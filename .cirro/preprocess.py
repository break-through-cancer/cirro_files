#!/usr/bin/env python3

from cirro.helpers.preprocess_dataset import PreprocessDataset
import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)

# 1. Get parameters from cirro pipeline call
ds = PreprocessDataset.from_running()
ds.logger.info("List of starting params")
ds.logger.info(ds.params)

ds.logger.info('checking ds.files')
files = ds.files
ds.logger.info(files.head())
ds.logger.info(files.columns)

# 2. Add samplesheet parameter and set equal to ds.samplesheet
ds.logger.info("Checking samplesheet parameter")
ds.logger.info(ds.samplesheet)

# ADD WORKFLOW CONFIG FOR SEGMENTATION AND DOWNSTREAM ANALYSIS TOOLS
# ds.add_param("segmentation", '"[unmicst, ilastik]"')
ds.add_param("segmentation", 'unmicst')
ds.add_param("downstream", '"[scimap, fastpg, flowsom, scanpy]"')

ds.logger.info(ds.params)