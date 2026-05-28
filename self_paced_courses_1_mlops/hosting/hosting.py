from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="self_paced_courses_1_mlops/deployment",
    repo_id=f"warnerjc/PIMA-Diabetes-Prediction", # read the Hugging Face username from HF_USER
    repo_type="space",
    path_in_repo="", # optional: subfolder path inside the repo
)
