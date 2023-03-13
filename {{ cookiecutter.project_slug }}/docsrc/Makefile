# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

AUTODOCBUILD  = sphinx-apidoc
MODULEDIR     = ../src/
AUTODOCDIR    = $(SOURCEDIR)/api

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help github clean doc-requirements Makefile

github:
	@make html
	@mkdir -p ../docs
	@cp -a $(BUILDDIR)/html/. ../docs

clean:
	rm -rf $(BUILDDIR)/* $(AUTODOCDIR)

$(AUTODOCDIR): #$(MODULEDIR)
	mkdir -p $@
	$(AUTODOCBUILD) -f -o $@ $(MODULEDIR)

doc-requirements: $(AUTODOCDIR)


# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: doc-requirements
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
