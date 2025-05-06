from cirro.helpers.preprocess_dataset import PreprocessDataset

if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    # Remove param validation to override dss_threads limit
    ds.add_param("validate_params", False)
