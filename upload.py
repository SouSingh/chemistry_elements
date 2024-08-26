from huggingface_hub import HfApi, HfFolder

# Replace with your information
hf_username = "Sourabh2"
dataset_name = "chemical_compund"
csv_file_path = "data.csv"

# Get your token from Hugging Face
token = HfFolder.get_token()

# Initialize HfApi
api = HfApi()

# Upload the CSV file
api.upload_file(
    path_or_fileobj=csv_file_path,
    path_in_repo=f"datasets/{hf_username}/{dataset_name}/compounds.csv",
    repo_id=f"{hf_username}/{dataset_name}",
    repo_type="dataset",
    token=token,
)
