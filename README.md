# PEPPER

## Setting the environment

The environment on our computer is as follows:
* Python 3.6
* pycaret 2.3.3
* Pandas 1.1.5
* NumPy 1.19.5
* scikit-learn 0.23.2

## Usage

```
python PEPPER.py --file "input fasta file" --threshold "prediction threshold, (0~1) default=0.5" --saveFeatures "save the features or not? [yes, no] default=no" --out "the predicted results folder"
```

For example:
```
python PEPPER.py example/input.fasta --threshold 0.5 --out example --saveFeatures no
```
## Cite

Please cite our paper if you use this code in your own work.
Li et al., "Computational analysis and prediction of PE_PGRS proteins using machine learning", Computational and structural biotechnology journal, 20:662-674, https://doi.org/10.1016/j.csbj.2022.01.019
