# Raw and Processed Datasets

## Raw Data
The raw ATAC-seq datasets are from [Lin et al. 2023](https://www.nature.com/articles/s41597-023-02373-y). Specifically, the following two datasets were downloaded from the supplementary files:

- [`Cell-type Peak Matrix .rds`](https://figshare.com/ndownloader/files/40957361): an RDS file that contains peaks of rows and cell types as columns.

- [`atac_all.metaData.txt`](https://ftp.cngb.org/pub/CNSA/data4/CNP0002827/Single_Cell/CSE0000120/atac_all.metaData.txt): meta data with different features for cells.


## Processed Data
Using the raw datasets, a normalized pseudo bulk matrix was created as saved as a csv file `psd.bulk.zfish_atac.10hpf.lg1x.csv`.

The raw dataset was preprocessed using `scripts/ATAC-Seq-Analysis-Step-3-subset-celltypes.Rmd` which was originally written by Xenia Sirodzha but adapted for the purposes of this work. Hence, you can download the raw datasets and run the aforementioned R-script to generate the processed dataset `psd.bulk.zfish_atac.10hpf.lg1x.csv`.


## References

- Lin, X., Yang, X., Chen, C., Ma, W., Wang, Y., Li, X., Zhao, K., Deng, Q., Feng, W., Ma, Y. and Wang, H., 2023. Single-nucleus chromatin landscapes during zebrafish early embryogenesis. _Scientific Data_, 10(1), p.464.