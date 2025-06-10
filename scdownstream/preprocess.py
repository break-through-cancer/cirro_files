#!/usr/bin/env python3

from cirro.helpers.preprocess_dataset import PreprocessDataset
import pandas as pd
import numpy as np

# 1. Get parameters from cirro pipeline call
ds = PreprocessDataset.from_running()
ds.logger.info("List of starting params")
ds.logger.info(ds.params)

ds.logger.info('checking ds.files')
ds.logger.info(ds.files.head())
ds.logger.info(ds.files.columns)

# 2. Add samplesheet parameter and set equal to ds.samplesheet
ds.logger.info("Checking samplesheet parameter")
ds.logger.info(ds.samplesheet)
samplesheet = ds.samplesheet
samplesheet['filtered'] = samplesheet['file']
ds.logger.info(ds.samplesheet)
samplesheet.to_csv('samplesheet.csv', index=None)
ds.add_param("input", "samplesheet.csv")

