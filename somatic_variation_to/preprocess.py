# from cirro.helpers.preprocess_dataset import PreprocessDataset

# def process_input_type(ds, input_type, bam_file, bam_dir, bam):
#     if ds.params.get(input_type) == "file":
#         ds.add_param(bam, ds.params.get(bam_file))
#         ds.remove_param(bam_file)
#     elif ds.params.get(input_type) == "directory":
#         ds.add_param(bam, ds.params.get(bam_dir))
#         ds.remove_param(bam_dir)

#     ds.remove_param(input_type)

# if __name__ == "__main__":
#     ds = PreprocessDataset.from_running()

#     process_input_type(ds, "input_type_tumor", "bam_tumor_file", "bam_tumor_directory", "bam_tumor")
#     process_input_type(ds, "input_type_normal", "bam_normal_file", "bam_normal_directory", "bam_normal")
#     ds.add_param("validate_params", False)
