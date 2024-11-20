from cirro.helpers.preprocess_dataset import PreprocessDataset

if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    if ds.params.get("input_type") == "file":
        ds.add_param("bam", ds.params.get("bam_file"))
        ds.remove_param("bam_file")
    else:
        ds.add_param("bam", ds.params.get("bam_directory"))
        ds.remove_param("bam_directory")
        
    ds.remove_param("input_type")
