def skip_logger(app, what, name, obj, skip, options):
    skip_conditions = [
        obj.name.startswith('log'),
        'test' in obj.name,
    ]
    for condition in skip_conditions:
        if condition:
            skip = True
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_logger)
