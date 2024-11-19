from cirro.helpers.preprocess_dataset import PreprocessDataset

if __name__ == "__main__":
    ds = PreprocessDataset.from_running()

    if ds.params.get("input_type_tumor") == "file":
        ds.add_param("bam_tumor", ds.params.get("bam_tumor_file"))
        ds.remove_param("bam_tumor_file")
    else:
        ds.add_param("bam_tumor", ds.params.get("bam_tumor_directory"))
        ds.remove_param("bam_tumor_directory")
        
    ds.remove_param("input_type_tumor")

    if ds.params.get("input_type_normal") == "file":
        ds.add_param("bam_normal", ds.params.get("bam_normal_file"))
        ds.remove_param("bam_normal_file")
    elif ds.params.get("input_type_normal") == "directory":
        ds.add_param("bam_normal", ds.params.get("bam_normal_directory"))
        ds.remove_param("bam_normal_directory")
        
    ds.remove_param("input_type_normal")
