#!/usr/bin/env python3

# adapted from https://github.com/break-through-cancer/btc-spatial-pipelines/blob/main/.cirro/preprocess.py

from cirro.helpers.preprocess_dataset import PreprocessDataset
import pandas as pd
import numpy as np

def make_manifest(ds: PreprocessDataset):
    """
    1. Create a samplesheet for my workflow
    2. Add samplesheet as a input parameter

    """

    samplesheet = ds.files[['sample', 'file']].rename(columns={'file': 'bam'}, inplace=False)
    samplesheet.to_csv('samplesheet.csv', index=False)

    ds.add_param("input", "samplesheet.csv")

if __name__ == '__main__':
    ds = PreprocessDataset.from_running()
    make_manifest(ds)

    ds.logger.info(ds.params)
    print(ds.params)