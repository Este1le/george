# -*- coding: utf-8 -*-

import os
import sys
import sphinx_rtd_theme

d = os.path.dirname
sys.path.insert(0, d(d(os.path.abspath(__file__))))
import george

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

# # FIXME
# mathjax_path = "MathJax/MathJax.js"

# General information about the project.
project = u"George"
copyright = u"2013-2014 Dan Foreman-Mackey"

version = george.__version__
release = george.__version__

exclude_patterns = ["_build"]
pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["_static"]