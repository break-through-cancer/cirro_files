#!/usr/bin/env python3

import pandas as pd

from cirro.helpers.preprocess_dataset import PreprocessDataset

def make_manifest(files: pd.DataFrame) -> pd.DataFrame:
    """
    Create a samplesheet for my workflow
    """
    samplesheet = files[['sample', 'file']].rename(columns={'file': 'bam'}, inplace=False)
    return samplesheet

if __name__ == '__main__':
    ds = PreprocessDataset.from_running()
    manifest = make_manifest(ds.files)
    manifest.to_csv('samplesheet.csv', index=False)