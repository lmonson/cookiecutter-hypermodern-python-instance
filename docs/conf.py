"""Sphinx configuration."""
project = "Hypermodern_Python_Template"
author = "Lynn Monson"
copyright = "2022, Lynn Monson"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
