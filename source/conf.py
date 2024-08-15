import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Test_app'
copyright = '2024, YaroslavTarnopil'
author = 'YaroslavTarnopil'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']

