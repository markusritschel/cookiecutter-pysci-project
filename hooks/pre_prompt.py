GREEN = "\033[92m"
BLUE  = "\033[94m"
RESET = "\033[0m"

msg = f"""
{GREEN}☝🏼 Important: You will now be asked to fill in some information about your project.
{RESET}
When asked for the project name [4], you may use a normal name with spaces, e.g. "My new Project". 
The project slug [5] (which is used for the directory name and the package name) will be generated 
automatically from the project name by replacing spaces with dashes and converting to lowercase, 
e.g. "my-new-project". For the python package name [6], remaining dashes will be replaced with 
underscores ("my_new_project") to ensure proper naming.
Of course, you can also directly specify the project slug and package name if you want to use a 
different naming convention.

{GREEN}👉🏼 Research Projects: {RESET}If you answer "yes" to the question "Is this a research project?" [7], some 
additional directories will be created for you (e.g. data, notebooks, references, results, src). 
If you answer "no", these directories will not be created.

Let's go 😃
"""
print(msg)
