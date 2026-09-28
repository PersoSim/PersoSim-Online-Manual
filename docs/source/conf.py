# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PersoSim'
html_show_copyright = False;

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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
]
numfig = True

html_theme_options = {
    'collapse_navigation': False,  
    'navigation_depth': 6,    
}

html_css_files = [
    'custom.css',
]

# MyST Parser Einstellungen (für Markdown)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "smartquotes",
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'de'

source_suffix = '.rst'

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_title = 'Dokumentation PersoSim'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# PDF erstellen
simplepdf_vars = {
    'primary': '#FA2323',
    'secondary': '#379683',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': 'FA2323',
    'cover-bg': 'url(cover-bg.jpg) no-repeat center',
    'cover-overlay': 'rgba(250, 35, 35, 0.5)',
    'top-left-content': 'counter(page)',
    'bottom-center-content': '"Custom footer content"',
}

latex_documents = [
    ('index', 'Dokumentation-PersoSim.tex', 'Dokumentation PersoSim', 'secunet Security Networks AG', 'documentation'),
]

latex_engine = 'pdflatex'

# latex_logo = 'path/to/logo.png'  # Optional: füge ein Logo ein