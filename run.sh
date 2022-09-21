#!/bin/bash
# run scripts for the project
if ! command -v conda &> /dev/null;then
    echo -e "The 'conda' command wasn't found, check this: https://conda.io/projects/conda/en/latest/user-guide/install/index.html."
    exit 1
fi
env="cadquery"

ENVS=$(conda env list | awk '{print $1}' )
# setup the conda env
# check if the conda env already exists before setup
#if [[ $ENVS = *"$env"* ]] ;then
#    conda create -n "$env"
#    conda activate "$env"
#    conda install -c conda-forge -c cadquery cadquery=master
#    conda deactivate
#fi
conda activate "$env"

# add support to change the params file to source
python3 main.py

conda deactivate
