"""Sphinx configuration."""

import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "setup.cfg"))

project = config.get("metadata", "name")
version = config.get("metadata", "version")
release = version  # Sphinx uses 'release' as the full version
author = config.get("metadata", "author")
email = config.get("metadata", "maintainer_email")
copyright = config.get("metadata", "copyright")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # sphinx_click must load before sphinx_autodoc_typehints. With Sphinx 9, the latter
    # imports the sphinx.ext.autodoc.mock submodule, which shadows the mock() function that
    # sphinx_click imports, so `.. click::` fails with "'module' object is not callable".
    "sphinx_click",
    "sphinx_autodoc_typehints",
]
html_theme = "furo"
html_context = {"version": version, "display_version": True}
