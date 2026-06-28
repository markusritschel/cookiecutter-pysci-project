# ==============================================
# Configuration for the Sphinx Immaterial theme
# https://sphinx-immaterial.readthedocs.io/
# ==============================================

extensions = [
    'sphinx_immaterial',
]


html_theme_options = {
    "sidebar_hide_name": False,
    'navigation_with_keys': True,
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://{{ cookiecutter.github_username}}.github.io/{{ cookiecutter.project_slug }}/",
    "repo_url": "https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/",
    "repo_name": "{{ cookiecutter.project_slug }}",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "navigation.tabs.sticky",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        "navigation.footer",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "search.suggest",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "content.code.copy",
        "content.action.edit",
        "content.action.view",
        "content.tooltips",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme)",
            "toggle": {
                "icon": "material/brightness-auto",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to system preference",
            },
        },
    ],
    # # BEGIN: version_dropdown
    # "version_dropdown": True,
    # "version_info": [
    #     {
    #         "version": "https://{{ cookiecutter.github_username}}.github.io/{{ cookiecutter.project_slug }}/",
    #         "title": "Github Pages",
    #         "aliases": [],
    #     },
    # ],
    # # END: version_dropdown
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/",
            "name": "Source on github.com",
        },
    ],
    # END: social icons
}
