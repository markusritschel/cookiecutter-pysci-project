# ========================================
# Configuration for the Sphinx Furo theme
# https://pradyunsg.me/furo/
# ========================================

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_theme_options = {
    "source_repository": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "red",
        "color-brand-content": "#CC3333",
        # "color-admonition-background": "orange",
    },
    "sidebar_hide_name": False,
    'navigation_with_keys': True,
    "top_of_page_buttons": ["edit"],
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
    "announcement": "<em>:🚀 Important</em> announcement!",
}

html_copy_source = False
html_show_sourcelink = False
