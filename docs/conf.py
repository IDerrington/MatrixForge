# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MatrixForge'
copyright = '2026, IDerrington'
author = 'IDerrington'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_nb',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = "MatrixForge"

html_theme_options = {
    "github_url": "https://github.com/IDerrington/MatrixForge",
    "show_nav_level": 2,
    "navigation_depth": 3,
    "show_toc_level": 2,
    "logo": { 
        "text": "MatrixForge",
    },
}

# -- MyST-NB configuration ---------------------------------------------------

# Configure MyST-NB to execute notebooks
nb_execution_mode = "auto"
nb_execution_timeout = 60

# MyST extensions
myst_enable_extensions = [
    "dollarmath",  # Enable $...$ for inline math
    "amsmath",     # Enable advanced math environments
    "colon_fence", # Enable ::: fences
]

