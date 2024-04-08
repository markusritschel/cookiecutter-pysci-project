#!/bin/bash
# TODO: Alternatively, implement this right in the Makefile!

# Extract the installed pip packages
pip_packages=$(conda env export | grep -A9999 ".*- pip:" | grep -v "^prefix: ")

# Export conda environment without builds
conda env export --from-history | grep -v "^prefix: " > environment.yml

# And append pip packages
echo "$pip_packages" >> environment.yml
