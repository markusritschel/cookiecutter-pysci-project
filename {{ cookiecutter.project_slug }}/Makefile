# This is a self-documenting Makefile.
# For details, check out the following resources:
# https://gist.github.com/klmr/575726c7e05d8780505a
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

# ======= Put your targets etc. between here and the line which is starting with ".DEFAULT_GOAL" =======
# Document any rules by adding a single line starting with ## right before the rule (see examples below)
# ======================================================================================================

include .env


.PHONY: clean clean-jupyter-book clean-pyc, clean-logs, docs, book, save-requirements, requirements, src-available, conda-env, test-requirements, tests, clear-images, convert-images, figures, crop-pdf, crop-png, show-help

## Clean python artifacts, logs and jupyter-book built
clean: clean-pyc clean-logs clean-jupyter-book clean-docs

clean-jupyter-book:
	jb clean --all docsrc/

clean-docs:
	jb clean --all reports/book/
	rm -rf docsrc/build/*

# Remove Python file artifacts
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


## Remove all log files
clean-logs:
	find ./logs -iname '*.log' -type f -exec rm {} +


## Build the code documentation with Sphinx
docs:
	$(MAKE) -C docsrc html


## Build the project's Jupyter-Book
book:
	jb build ./reports/book


## Update the requirements.txt
save-requirements:
	pip freeze > requirements.txt


## Install Python Dependencies via pip
requirements:
	python -m pip install -U pip setuptools wheel
	mamba install --file requirements.txt
	pip install sphinxcontrib-napoleon2 rinohtype sphinx-rtd-theme sphinx-autodoc-defaultargs nbsphinx myst-parser sphinx-issues sphinxcontrib-bibtex
	# python -m pip install -r requirements.txt


## Make the source code as package available
src-available:
	python setup.py develop


## Create a conda environment named after the project slug and activate it
conda-env:
	echo "Create conda environment `{{ cookiecutter.project_slug }}`"
	mamba env create --file environment.yml
	echo "Activate conda environment `{{ cookiecutter.project_slug }}`"
	mamba activate {{ cookiecutter.project_slug }}


## Check if all packages listed in requirements.txt are installed in the current environment
test-requirements:
	@echo "Check if all packages listed in requirements.txt are installed in the current environment:"
	# the "|| true" prevents the command returning an error if grep does not find a match
	python -m pip -vvv freeze -r requirements.txt | grep "not installed" || true


## Run pytest for the source code
tests: test_requirements
	pytest src/tests/ --doctest-modules -v


.SUFFIXES: .jpg .jpeg .png .pdf
imagedir = ./reports/figures

JPEG=$(wildcard ${imagedir}/*.jpg ${imagedir}/*.jpeg)		# find all JPG and JPEG files
JPG=$(JPEG:.jpeg=.jpg)						# internally rename all JPEG to JPG
PDF=$(wildcard ${imagedir}/*.pdf) 				# find all PDF files
jpg2png=$(JPG:.jpg=.png)					# naming rule for JPG to PNG conversion
pdf2png=$(PDF:.pdf=.png)					# naming rule for PDF to PNG conversion

## Remove all PNG files that have a PDF or JPG parent
clear-images:
	@echo remove all PNG files in ${imagedir} which have a PDF or JPG parent
	@rm -f ${pdf2png}
	@rm -f ${jpg2png}


## Convert JPG and PDF files to PNG files
convert-images: $(jpg2png) $(pdf2png)
	@echo ---
	@echo finished conversion


# rule for converting JPG and PDF to PNG
# compare compression result and delete PNG if result is bad
.jpeg.png .jpg.png .pdf.png:
	@convert -density 400 "$<" -resize 800x800 -quality 85% "$@"
	@echo converted $<
	@i=`stat -c%s "$<"`; \
	 o=`stat -c%s "$@"`; \
	 score=$$(( $$i / $$o)); \
	 [ $$score -lt 2 ] && echo "\tbad compression: remove $@" && rm $@ || true

# @i=`stat -c%s "$<"`; \
# o=`stat -c%s "$@"`; \
# [ $$((2*o)) -gt $$i ] && echo "\tbad compression: remove $@" && rm -f $@ || true


## Clear all PNGs with a JPG or PDF parent, crops PDF files, converts to PNG, and crops PNGs
figures: clear_images crop_pdf convert crop_png
	@echo ---
	@echo finished creating figures


## Crop PDF files
crop-pdf:
	@echo
	@echo crop all pdf files in ${imagedir}
	@for file in `find ${imagedir}/ -iname "*.pdf" -type f`; \
		do \
			pdfcrop $${file} $${file}; \
		done;


## Crop PNG files
crop-png:
	@echo
	@echo crop all png files in ${imagedir}
	@for file in `find ${imagedir}/ -iname "*.png" -type f`; \
		do \
			echo crop $${file}; \
			convert $${file} -trim $${file}; \
		done;
	


# ==================== Don't put anything below this line ====================
# https://www.digitalocean.com/community/tutorials/how-to-use-makefiles-to-automate-repetitive-tasks-on-an-ubuntu-vps
.DEFAULT_GOAL := show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)";echo;sed -ne"/^## /{h;s/.*//;:d" -e"H;n;s/^## //;td" -e"s/:.*//;G;s/\\n## /---/;s/\\n/ /g;p;}" ${MAKEFILE_LIST}|LC_ALL='C' sort -f|awk -F --- -v n=$$(tput cols) -v i=19 -v a="$$(tput setaf 6)" -v z="$$(tput sgr0)" '{printf"%s%*s%s ",a,-i,$$1,z;m=split($$2,w," ");l=n-i;for(j=1;j<=m;j++){l-=length(w[j])+1;if(l<= 0){l=n-i-length(w[j])-1;printf"\n%*s ",-i," ";}printf"%s ",w[j];}printf"\n";}'|more
