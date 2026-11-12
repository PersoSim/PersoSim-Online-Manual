"""Sphinx extension: profile tables generated from the PersoSim profile data.

Data sources (paths relative to the Sphinx source directory):

* ``_data/generated-docs/persosim-profiles.tsv``: written by the PersoSim build
  (one row per profile, columns "Profile", "DG1" ... "DG20", PIN etc.). The file
  is copied unchanged from the build output; this extension converts the values
  for display (date format, absent data groups, leading/trailing spaces).
* ``_data/profile-notes.tsv``: German description ("Besonderheiten") per profile,
  maintained by hand; columns "Profil" and "Besonderheiten".

In a page, the directive

    ```{profile-table} nPA_
    ```

inserts the profiles whose name starts with the given prefix in two views:

* HTML: one wide comparison table with a column per profile,
* LaTeX and simplepdf: one narrow two-column table per profile, because the
  wide table does not fit on a PDF page.

A field row is left out of a group when no profile of the group has it, e.g.
DG19/DG20 outside the eAT profiles.
"""
import csv
import io
import unicodedata
from pathlib import Path

from docutils import nodes
from sphinx import addnodes
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)

PROFILES_FILE = Path('_data') / 'generated-docs' / 'persosim-profiles.tsv'
NOTES_FILE = Path('_data') / 'profile-notes.tsv'

# Columns of the PersoSim TSV shown in the tables, with their German labels
FIELDS = [
    ('DG1', 'Dokumenttyp (DG1)'),
    ('DG2', 'Ausgebender Staat (DG2)'),
    ('DG3', 'Gültig bis (DG3)'),
    ('DG4', 'Vorname(n) (DG4)'),
    ('DG5', 'Familienname (DG5)'),
    ('DG6', 'Ordens-/Künstlername (DG6)'),
    ('DG7', 'Doktorgrad (DG7)'),
    ('DG8', 'Geburtsdatum (DG8)'),
    ('DG9', 'Geburtsort (DG9)'),
    ('DG10', 'Staatsangehörigkeit (DG10)'),
    ('DG13', 'Geburtsname (DG13)'),
    ('DG17', 'Anschrift (DG17)'),
    ('DG18', 'Wohnort-ID (DG18)'),
    ('DG19', 'Nebenbestimmungen I (DG19)'),
    ('DG20', 'Nebenbestimmungen II (DG20)'),
]
DATE_FIELDS = {'DG3', 'DG8'}
NOTES_LABEL = 'Besonderheiten'

ABSENT = '<absent>'               # marker in the PersoSim TSV
NOT_PRESENT = '(nicht vorhanden)'  # shown in the tables
EDGE_SPACE = '␣'                   # visible marker for a leading/trailing space

# Longest run of characters without a space kept on one line in the PDF view
CHUNK = 38
# Column widths (percent) of the per-profile tables in the PDF view
PDF_WIDTHS = (32, 68)


def read_tsv(path):
    """Return the records of a tab-separated file as lists of strings.

    Accepts UTF-8 (with or without BOM) and UTF-16 with BOM, and the quoting that
    spreadsheet programs add when saving (a value with a double quote is written
    as "...""...").
    """
    raw = path.read_bytes()
    if raw.startswith((b'\xff\xfe', b'\xfe\xff')):
        text = raw.decode('utf-16')
    else:
        text = raw.decode('utf-8-sig')
    return [r for r in csv.reader(io.StringIO(text, newline=''), delimiter='\t') if any(c.strip() for c in r)]


def display_value(column, value):
    """Convert a raw PersoSim value into the form shown in the tables."""
    if value == ABSENT:
        return NOT_PRESENT
    if column in DATE_FIELDS and len(value) == 8 and value[:4].isdigit():
        # YYYYMMDD, unknown parts as spaces -> YYYY-MM-DD with XX
        value = value.replace(' ', 'X')
        return f'{value[:4]}-{value[4:6]}-{value[6:]}'
    lead = len(value) - len(value.lstrip(' '))
    trail = len(value) - len(value.rstrip(' '))
    if lead == len(value):
        return EDGE_SPACE * lead
    return EDGE_SPACE * lead + value.strip(' ') + EDGE_SPACE * trail


def load_profiles(profiles_path, notes_path):
    """Return (labels, rows, names without a description); each row is [name, notes, field values...]."""
    records = read_tsv(profiles_path)
    header = records[0]
    missing = [c for c in ['Profile'] + [c for c, _ in FIELDS] if c not in header]
    if missing:
        raise ValueError(f'{profiles_path}: missing columns {", ".join(missing)}')
    notes = {r[0]: (r[1] if len(r) > 1 else '') for r in read_tsv(notes_path)[1:]}
    rows, undescribed = [], set()
    for record in records[1:]:
        record += [''] * (len(header) - len(record))
        cells = dict(zip(header, record))
        name = cells['Profile'].removesuffix('.perso')
        if name not in notes:
            undescribed.add(name)
        rows.append([name, notes.get(name, '')] + [display_value(c, cells[c]) for c, _ in FIELDS])
    labels = ['Profil', NOTES_LABEL] + [label for _, label in FIELDS]
    return labels, rows, undescribed


def units(text):
    """Visible characters: a base character with its combining marks is one unit."""
    out = []
    for ch in text:
        if out and unicodedata.combining(ch):
            out[-1] += ch
        else:
            out.append(ch)
    return out


def wrapped_lines(value):
    """Split runs longer than CHUNK characters into separate lines (PDF view only)."""
    lines, cur = [], ''
    for word in value.split(' '):
        us = units(word)
        while len(us) > CHUNK:
            if cur:
                lines.append(cur)
                cur = ''
            lines.append(''.join(us[:CHUNK]))
            us = us[CHUNK:]
        w = ''.join(us)
        cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return lines


def cell(value, wrap=False):
    entry = nodes.entry()
    para = nodes.paragraph()
    if wrap:
        for k, line in enumerate(wrapped_lines(value)):
            if k:
                # forced line break; each output format only uses its own raw node
                para += nodes.raw('', '\\newline ', format='latex')
                para += nodes.raw('', '<br/>', format='html')
            para += nodes.Text(line)
    elif value:
        para += nodes.Text(value)
    entry += para
    return entry


def table(header, rows, widths=None):
    tbl = nodes.table()
    group = nodes.tgroup(cols=len(header))
    tbl += group
    for k in range(len(header)):
        group += nodes.colspec(colwidth=widths[k] if widths else 1)
    if widths:
        tbl['classes'].append('colwidths-given')
    thead = nodes.thead()
    head_row = nodes.row()
    for title in header:
        head_row += cell(title)
    thead += head_row
    group += thead
    tbody = nodes.tbody()
    for values in rows:
        row = nodes.row()
        for k, value in enumerate(values):
            row += cell(value, wrap=bool(widths) and k > 0)
        tbody += row
    group += tbody
    return tbl


class ProfileTable(SphinxDirective):
    required_arguments = 1
    has_content = False

    def data_path(self, relative):
        rel, path = self.env.relfn2path(str(Path('/') / relative), self.env.docname)
        self.env.note_dependency(rel)
        return Path(path)

    def run(self):
        prefix = self.arguments[0]
        labels, rows, undescribed = load_profiles(self.data_path(PROFILES_FILE), self.data_path(NOTES_FILE))
        profiles = [r for r in rows if r[0].startswith(prefix)]
        if not profiles:
            raise self.error(f'no profile in {PROFILES_FILE} starts with "{prefix}"')
        for p in profiles:
            if p[0] in undescribed:
                logger.warning(f'no description for profile {p[0]} in {NOTES_FILE.as_posix()}',
                               location=self.get_location())
        fields = [k for k in range(1, len(labels))
                  if any(p[k] != NOT_PRESENT for p in profiles)]

        html = addnodes.only(expr='html')
        html += table(['Feld'] + [p[0] for p in profiles],
                      [[labels[k]] + [p[k] for p in profiles] for k in fields])

        pdf = addnodes.only(expr='latex or simplepdf')
        for p in profiles:
            pdf += nodes.rubric(text=p[0])
            pdf += table(['Feld', 'Wert'], [[labels[k], p[k]] for k in fields], widths=PDF_WIDTHS)
        return [html, pdf]


def setup(app):
    app.add_directive('profile-table', ProfileTable)
    return {'version': '1.1', 'parallel_read_safe': True, 'parallel_write_safe': True}
