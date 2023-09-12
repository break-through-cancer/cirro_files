#!/usr/bin/env python3

import json
from cirro.helpers.preprocess_dataset import PreprocessDataset
from cirro.api.models.s3_path import S3Path
import logging

def setup_inputs(ds: PreprocessDataset):    
    # turn comma separated string of normal_bams into list
    ds.params[
        "CNVSomaticPanelWorkflow.normal_bams"
    ] = ds.params.get(
        "CNVSomaticPanelWorkflow.normal_bams",
        "normal_bams"
    ).split(',')

    # turn comma separated string of normal_bais into list with .bai suffix
    ds.params[
        "CNVSomaticPanelWorkflow.normal_bais"
    ] = [x + ".crai" for x in ds.params.get(
        "CNVSomaticPanelWorkflow.normal_bais",
        "normal_bais"
    ).split(',')]

def setup_options(ds: PreprocessDataset):

    # Add default params
    ds.add_param("memory_retry_multiplier", 2.0)
    ds.add_param("use_relative_output_paths", True)

    # Set up the scriptBucketName
    ds.add_param(
        "scriptBucketName",
        S3Path(ds.params['final_workflow_outputs_dir']).bucket
    )

    # Isolate the options arguments for the workflow
    options = {
        kw: val
        for kw, val in ds.params.items()
        if not kw.startswith("ConvertPairedFastQsToUnmappedBamWf")
    }

    # Write out
    with open("options.json", "wt") as handle:
        json.dump(options, handle, indent=4)


if __name__ == "__main__":
    ds = PreprocessDataset.from_running()
    setup_inputs(ds)
    setup_options(ds)