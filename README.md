# Lab Rotation Research

## Overview

This repository contains documentation and code for my lab rotation research titled _"Understanding Cis-Regulatory Control of Neural Crest Cell Development with Deep Learning"_.

## Contents

The repository has the following folders:

- `data/` - Datasets
- `notebooks/` - Notebooks used for data analysis
- `notes/` - Research notes
- `results/` -  Processed data outputs, graphs, and figures.
- `scripts/` - Analysis scripts
- `src/` -  Python files with modules, classes, functions that can be imported into scripts and notebooks 

## Introduction

Neural crest cells (NCCs) are multipotent cells that were first described in 1886 as "Zwischenstrang" (the intermediate strand) by the Swiss embryologist Wilheim His ([Achilleos et.al., 2012](https://www.nature.com/articles/cr201211)). The name "Zwischenstrang" stems from the their location betweeen the dorsal ectoderm and the neural tube in vertebrate embryos, but was later renamed to neural crest cells by Arthur Milnes Marshall due to the more precise description of its anatomical position along the border of the neural plate during early verbrate development ([Achilleos et.al., 2012](https://www.nature.com/articles/cr201211), [Soto et.al., 2012](https://stemcellsjournals.onlinelibrary.wiley.com/doi/10.1002/sctm.20-0361)). 
NCCs are transient, multipotent cells that are capable of forming diverse cell types during vertebrate embryogenesis ([Fabian et.al., 2022](https://www.nature.com/articles/s41467-021-27594-w)). Due to the extraordinary multipotent abilities of NCCs, understanding the underlying transcription factors  NCCs could lead to understanding of key cells during vertebrate embryogenesis. 


## Data

## Methodology

## Results

## Discussion

## **Quick Start**
To get started with this project, do the following in the terminal:

1. **Clone the repository:**
```bash
git clone https://github.com/sasselab/Rotation_VictorEmenike_2025-03-03.git
```

2. **Navigate to the project directory:**
```bash
cd Rotation_VictorEmenike_2025-03-03
```

3. **Create a virtual environment:**

Ensure you have a Python environment set up. You can create a virtual environment (e.g. `lab_rotation`) using conda as follows:

```bash
conda create -n lab-rotation python=3.9
```

```bash
conda activate lab-rotation
```

4. **Install required packages**

```bash
pip install -e .
```

This will run the file `setup.py`, install a package called `stf_tools` that contains relevant functions used and required packages. The `stf_tools` is located in the folder `src`. 

5. **Running the pipeline**

- Navigate to the folder `notebooks`. Open the jupyter notebook `multi_task_model_ConvMLPModel.ipynb`. To train the model from scratch, set `training = True ` in the notebook.



## References

1. Achilleos, A. and Trainor, P.A., 2012. Neural crest stem cells: discovery, properties and potential for therapy. _Cell research_, 22(2), pp.288-304.

2. Soto, J., Ding, X., Wang, A. and Li, S., 2021. Neural crest-like stem cells for tissue regeneration. _Stem Cells Translational Medicine_, 10(5), pp.681-693.

3. Fabian, P., Tseng, K.C., Thiruppathy, M., Arata, C., Chen, H.J., Smeeton, J., Nelson, N. and Crump, J.G., 2022. Lifelong single-cell profiling of cranial neural crest diversification in zebrafish. _Nature communications, 13(1)_, p.13.