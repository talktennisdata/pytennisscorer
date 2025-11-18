"""Configuration file for the Sphinx documentation builder."""

import os
import sys
from datetime import datetime

# Add the source directory to the path
sys.path.insert(0, os.path.abspath("../src"))

# Project information
project = "pytennisscorer"
copyright = f"{datetime.now().year}, Robert Seidl"
author = "Robert Seidl"
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "myst_parser",
]

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
    "inherited-members": False,
}

autodoc_typehints = "both"
autodoc_typehints_format = "short"
autodoc_typehints_description_target = "documented"

# Autosummary settings
autosummary_generate = True

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_attr_annotations = True

# MyST settings (for markdown support)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Intersphinx mapping (link to other docs)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Source suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Master document
master_doc = "index"

# Templates path
templates_path = ["_templates"]

# Patterns to exclude
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# Language
language = "en"

# Theme options
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#2980B9",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# Static files
html_static_path = ["_static"]

# Sidebar options
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}

# Additional options
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
html_favicon = None
html_logo = None

# Copy button configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

# Output options
htmlhelp_basename = "pytennisscorerdoc"

# LaTeX options
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "figure_align": "htbp",
}

latex_documents = [
    (master_doc, "pytennisscorer.tex", "pytennisscorer Documentation", "Robert Seidl", "manual"),
]

# Man page options
man_pages = [(master_doc, "pytennisscorer", "pytennisscorer Documentation", [author], 1)]

# Texinfo options
texinfo_documents = [
    (
        master_doc,
        "pytennisscorer",
        "pytennisscorer Documentation",
        author,
        "pytennisscorer",
        "A Python package for tennis match scoring.",
        "Miscellaneous",
    ),
]

# Epub options
epub_title = project
epub_exclude_files = ["search.html"]
