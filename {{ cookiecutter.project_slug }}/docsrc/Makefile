# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
# SPHINXPROJ    = {{ cookiecutter.project_slug }}
SOURCEDIR     = source
BUILDDIR      = _build

AUTODOCBUILD  = sphinx-apidoc
MODULEDIR     = ../src/
AUTODOCDIR    = $(SOURCEDIR)/api


# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help github clean doc-requirements Makefile

clean:
	rm -rf $(BUILDDIR)/* $(AUTODOCDIR)

github:
	@make html
	@mkdir -p ../docs
	@cp -a $(BUILDDIR)/html/. ../docs

$(AUTODOCDIR): #$(MODULEDIR)
	mkdir -p $@
	$(AUTODOCBUILD) -f -o $@ $(MODULEDIR)

doc-requirements: $(AUTODOCDIR)


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile
%: doc-requirements
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
