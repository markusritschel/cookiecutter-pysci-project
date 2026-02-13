extensions = [
    'autoapi.extension',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
]


autoapi_dirs = ['../src/']
# autoapi_python_use_implicit_namespaces = True
autoapi_python_class_content = 'both'
autoapi_keep_files = False
autoapi_root = 'api'
# autoapi_template_dir = '_autoapi_templates'
# autoapi_ignore = []
autoapi_options = [
    'show-module-summary', 
    # 'show-inheritance', 
    # 'show-inheritance-diagram',
    'members', 
    'undoc-members', 
    # 'private-members', 
    'imported-members', 
    'inherited-members', 
]
autoapi_member_order = 'groupwise'


# Skip certain members
# https://sphinx-autoapi.readthedocs.io/en/latest/how_to.html#connect-to-the-autoapi-skip-member-event
def skip_members(app, what, name, obj, skip, options):
    try:
        skip_conditions = [
            obj.name.startswith('log'),
            name.endswith("FileSourceType"),  # Hack to prevent error from sphinx.ext.viewcode, which currently doesn't work with enum classes
        ]
        for condition in skip_conditions:
            if condition:
                skip = True
    except:
        pass
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_members)
