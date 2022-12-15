#!/usr/bin/env python
#_*_coding:utf-8_*_

import argparse
import re
from codes import Predict
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="Predict PE_PGRS proteins")
    parser.add_argument("--file", required=True, help="input fasta file")
    parser.add_argument("--threshold", default=0.5, help="prediction threshold, (0~1) default=0.5")
    parser.add_argument("--saveFeatures", default=False, help="save the features or not? [yes, no] default=no")
    parser.add_argument("--out", required=True, help="the predicted results folder")
    args = parser.parse_args()
    results = Predict.PGRS_predict(args.file, args.threshold, args.saveFeatures, args.out)
    results.to_csv(args.out + "/results.csv", index=None)
    print(results)
    print("Completed!")