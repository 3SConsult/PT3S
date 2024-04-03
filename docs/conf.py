# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath(r'C:\Users\jablonski\3S\PT3S'))


project = 'PT3S'
copyright = '2024, 3S Consult GmbH'
author = '3S Consult GmbH'
release = '90.14.15.0.dev1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.viewcode', 'sphinx.ext.doctest','nbsphinx']

todo_include_todos=True

templates_path = [r'C:\Users\jablonski\3S\PT3S']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
# This function will be called before Sphinx starts to build documents.
def setup(app):
    # Call nbconvert via subprocess to convert your notebook to rst format
    subprocess.call(['jupyter', 'nbconvert', '--to', 'rst','Example1.ipynb'])
    subprocess.call(['jupyter', 'nbconvert', '--to', 'rst','Example2.ipynb'])


