---
icon: material/snake
---

# Snakemake

Going one step further, in addition or as an alternative to `make`, [Snakemake](https://snakemake.readthedocs.io) provides even more extended functionalities.
Snakemake is pure Python, making it very convenient to work with and providing all the functionality of Python in your Snakemake workflow.
In Snakemake you define dependencies not as an "artificial" target but you indicate the target file you want to create, and Snakemake takes care of producing the required dependencies.
Another strength of Snakemake is that it is easily scalable:
Porting your Snakemake workflow from your local machine to a High-Performance Computing system is as straightforward as adding a few extra parameters to the executed command.
This way, Snakemake automatically generates bash scripts and submits them as jobs on the HPC, automatically distributing the tasks of the workflow.