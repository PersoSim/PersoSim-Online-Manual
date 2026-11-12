# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PersoSim'
# PersoSim version described by this manual. This is the only place where the
# current version is maintained: the sidebar header, the browser title, the PDF
# title page and the Markdown pages (via MyST substitutions, see below) use it.
release = '1.8.0'
version = '.'.join(release.split('.')[:2])
html_show_copyright = False;

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
from pathlib import Path

# Local extensions (profile tables from _data/generated-docs/persosim-profiles.tsv and _data/profile-notes.tsv); no __pycache__ in the source tree
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent / '_ext'))

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid',
    'myst_parser',
    'sphinx_simplepdf',
    'profile_tables',
]
numfig = True

html_theme_options = {
    'collapse_navigation': False,  
    'navigation_depth': 6,    
}

html_css_files = [
    'custom.css',
]

# MyST parser settings (for Markdown)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "smartquotes",
    "substitution",
]

# Values usable in the Markdown pages as {{ name }}
_release_url = f'https://github.com/PersoSim/PersoSim/releases/tag/{release}'
myst_substitutions = {
    'release': release,
    # GitHub release page with the archives for all platforms
    'release_url': f'[{_release_url}]({_release_url})',
}

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'de'

source_suffix = '.rst'

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_title = f'Dokumentation PersoSim {release}'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# PDF output
# File name of the generated PDF (simplepdf builder); the LaTeX PDF uses the same name, see latex_documents
simplepdf_file_name = f'Persosim_{release}.pdf'

simplepdf_vars = {
    'primary': '#FA2323',
    'secondary': '#379683',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': 'FA2323',
    'cover-bg': 'url(cover-bg.jpg) no-repeat center',
    'cover-overlay': 'rgba(250, 35, 35, 0.5)',
    'top-left-content': 'counter(page)',
    'bottom-center-content': f'"PersoSim {release}"',
}

latex_documents = [
    ('index', f'Persosim_{release}.tex', 'Dokumentation PersoSim', 'secunet Security Networks AG', 'manual'),
]

# XeLaTeX handles the Unicode characters in the profile data (combining marks, Greek etc.)
latex_engine = 'xelatex'

# Break overlong lines in code blocks (e.g. hex strings) instead of running off the page
latex_elements = {
    'sphinxsetup': 'verbatimforcewraps=true, verbatimmaxunderfull=0',
}

# latex_logo = 'path/to/logo.png'  # Optional: add a logo

# -- Options for the linkcheck builder ---------------------------------------

# Links to a locally running PersoSim (e.g. the SOAP WSDL) cannot be checked
linkcheck_ignore = [
    r'http://localhost[:/]',
]
