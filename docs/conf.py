# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test GH pages'
copyright = '2024, Christian Wansing'
author = 'Christian Wansing'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx_multiversion",
]

# -- Sphinx Multiversion --------------------------------------------------
# https://holzhaus.github.io/sphinx-multiversion/master/configuration.html#
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^(main|release/.*)$'
smv_remote_whitelist = r'^(origin|upstream)$'

templates_path = ['_templates']

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/versions.html",
        "sidebar/scroll-end.html",
    ],
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
