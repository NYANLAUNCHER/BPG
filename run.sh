#!/bin/bash
if ! command -v conda &> /dev/null;then
    echo -e "You should install conda, check this: "
fi

conda_setup() {
    conda create -n cadquery
    conda activate cadquery
    conda install -c conda-forge -c cadquery cadquery=master
    conda deactivate
}

generate() {
}

case $1 in
    # generate model(s)
    ""|"gen"|"generate") generate;;
    "conda"|"conda_setup") ;;
esac
