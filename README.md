# Lab Rotation Research

## Overview

This repository contains documentation and code for my lab rotation research titled _"Understanding Cis-Regulatory Control of Neural Crest Cell Development with Deep Learning"_.

## Contents

The repository has the following key folders:

- `data/` - Datasets
- `notebooks/` - Notebooks used for data analysis
- `notes/` - Research notes
- `results/` -  Processed data outputs, graphs, and figures.
- `scripts/` - Analysis scripts
- `src/` -  Python files with modules, classes, functions that can be imported into scripts and notebooks 

## Introduction

Neural crest cells (NCCs) are transient, multipotent cells that are capable of forming diverse cell types during vertebrate embryogenesis ([Fabian et.al., 2022](https://www.nature.com/articles/s41467-021-27594-w)).  NCCs were first described in 1886 as "Zwischenstrang" (the intermediate strand) by the Swiss embryologist Wilheim His due to their location betweeen the dorsal ectoderm and the neural tube in vertebrate embryos, but were later renamed to neural crest cells by Arthur Milnes Marshall due to the more precise description of its anatomical position along the border of the neural plate during early verbrate development ([Achilleos et.al., 2012](https://www.nature.com/articles/cr201211), [Soto et.al., 2012](https://stemcellsjournals.onlinelibrary.wiley.com/doi/10.1002/sctm.20-0361)). While most authors label NCCs as stem cells, [Achilleos et.al., 2012](https://www.nature.com/articles/cr201211) states that the majority of NCCs are actually progenitor cells. Despite the semantic nuances, identifying the underlying transcription factors/regulatory motifs that are crucial for the multipotency of NCCs will lead to broadening our understanding of vertebrate development and disease. 

Recent advances in large-scale functional genomic datasets and deep learning have led to **sequence-to-function models** ([Sasse et.al., 2024](https://www.nature.com/articles/s41592-024-02331-5)). Sequence-to-function models are typically supervised machine learning approaches that utilize deep learning architectures (convolutional neural networks or transformers) to learn a mapping between DNA sequence (inputs) and functional readouts (outputs) such as chromatin accessibility, ATAC peaks, histone modification, gene expression, etc. ([Sasse et.al., 2024](https://www.nature.com/articles/s41592-024-02331-5)). Once this mapping is learnt, the models can be used to predict the impact of various genetic variations  on the gene regulation of various cell types. Furthermore, explainable AI (xAI) approaches can be applied to these models to identify key regulatory motifs that are associated with the specfic functional readouts ([Novakovsky et.al., 2023](https://www.nature.com/articles/s41576-022-00532-2)).  Therefore, the goal of this work is to ascertain if such sequence-to-function models could be used to elucidate the key transcription factors/regulatory motifs that are crucial for neural crest cells.


![neural crest cells](media/neural_crest_cells.svg)

## Data

The main dataset used in this work is a single-nucleus assay for transposase-accessible chromatin with high throughput sequencing (snATAC-seq) dataset during zebrafish early embryogenesis ([Lin et.al., 2023](https://www.nature.com/articles/s41597-023-02373-y)). The snATAC-seq was generated at seven different time points of the first day of zebrafish embryogenesis, leading to accessibility profiles for 51,620 nuclei. The following two datasets were downloaded from the supplementary files:

- [`Cell-type Peak Matrix .rds`](https://figshare.com/ndownloader/files/40957361): an RDS file that contains peaks of rows and cell types as columns.

- [`atac_all.metaData.txt`](https://ftp.cngb.org/pub/CNSA/data4/CNP0002827/Single_Cell/CSE0000120/atac_all.metaData.txt): meta data with different features for cells.

In summary, the raw data consists of ATAC peak data for 15 cell types in 370058 chromosome locations within the zebrafish (_Danio rerio_) genome. These datasets was preprocessed using `scripts/ATAC-Seq-Analysis-Step-3-subset-celltypes.Rmd` which was originally written by Xenia Sirodzha but adapted for the purposes of this work. The preprocessed dataset consist of a pseudo-bulked matrix which contains the ATAC peaks of each cell type per chromosome location and a bed file `chromosomes.10hpf.bed` that contains the chromosomes locations of the ATAC peaks in the zebra genome. These two files were saved locally in the [data](https://github.com/sasselab/Rotation_VictorEmenike_2025-03-03/tree/main/data) folder, but due to the large file size of `psd.bulk.zfish_atac.10hpf.lg1x.csv`, it was only saved locally but not saved in this repository. Nevertheless, the user can download the raw datasets and run the aforementioned R-script to generate the processed dataset `psd.bulk.zfish_atac.10hpf.lg1x.csv`.

After pseudo-bulking, it was observed that cells in the central nervous system consistently had higher peaks than the other cell types. This could lead to increased sensitivity for these cell types after training the deep learning model. As such, the pseudo-bulked ATAC peaks were further normalized by using quantile normalization and saved as the file `normalized_peaks.csv` in the [data](https://github.com/sasselab/Rotation_VictorEmenike_2025-03-03/tree/main/data) folder. Similarly, due to large file size of `normalized_peaks.csv`, it was only saved locally and not in this repository. Nonetheless, `normalized_peaks.csv` can be generated by running the `atac_seq_analysis.ipynb` notebook in the [notebooks](https://github.com/sasselab/Rotation_VictorEmenike_2025-03-03/tree/main/notebooks) folder. 

![ATAC data](media/zebrafish_ATACseq_data.svg)

![normalized data](media/quantile_normalization.svg)

## Methodology

### Sequence-to-function modelling with gReLU

![seq2fxn_modelling](media/seq2fxn_modelling.svg)

![gReLU workflow with caption](media/grelu_workflow_w_caption.svg)

###  Model interpretation with integrated gradients
![integrated gradients](media/integrated_gradients.svg)

## Results

### Model performance

### Sequence-to-function identifies key regulatory motifs for neural crest cells

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

1. Achilleos, A. and Trainor, P.A., 2012. Neural crest stem cells: discovery, properties and potential for therapy. _Cell research, 22(2)_, pp.288-304.

2. Soto, J., Ding, X., Wang, A. and Li, S., 2021. Neural crest-like stem cells for tissue regeneration. _Stem Cells Translational Medicine, 10(5)_, pp.681-693.

3. Fabian, P., Tseng, K.C., Thiruppathy, M., Arata, C., Chen, H.J., Smeeton, J., Nelson, N. and Crump, J.G., 2022. Lifelong single-cell profiling of cranial neural crest diversification in zebrafish. _Nature communications, 13(1)_, p.13.

4. Sasse, A., Chikina, M. and Mostafavi, S., 2024. Unlocking gene regulation with sequence-to-function models. _Nature methods, 21(8)_, pp.1374-1377.

5. Novakovsky, G., Dexter, N., Libbrecht, M.W., Wasserman, W.W. and Mostafavi, S., 2023. Obtaining genetics insights from deep learning via explainable artificial intelligence. _Nature Reviews Genetics, 24(2)_, pp.125-137.

6. Lin, X., Yang, X., Chen, C., Ma, W., Wang, Y., Li, X., Zhao, K., Deng, Q., Feng, W., Ma, Y. and Wang, H., 2023. Single-nucleus chromatin landscapes during zebrafish early embryogenesis. _Scientific Data, 10(1)_, p.464.

7. Sasse, A., Ng, B., Spiro, A.E., Tasaki, S., Bennett, D.A., Gaiteri, C., De Jager, P.L., Chikina, M. and Mostafavi, S., 2023. Benchmarking of deep neural networks for predicting personal gene expression from DNA sequence highlights shortcomings. _Nature genetics, 55(12)_, pp.2060-2064.

8. Lal, A., Gunsalus, L., Nair, S., Biancalani, T. and Eraslan, G., 2024. gReLU: A comprehensive framework for DNA sequence modeling and design. _bioRxiv_, pp.2024-09.