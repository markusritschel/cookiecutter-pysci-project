extensions = [
    "autodoc2"
]

# autodoc2_module_summary = True
autodoc2_packages = [
    "../src/mypackage",
]

# Render API pages as MyST Markdown
autodoc2_render_plugin = "myst"

# Parse all docstrings as MyST
autodoc2_docstring_parser_regexes = [
    (r".*", "myst"),
]

# Output location
autodoc2_output_dir = "api"
