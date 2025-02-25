import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

main_dir = "src"

temp = [
    ".github/workflows/.gitkeep",
    f'{main_dir}/__init__.py',
    f'{main_dir}/components/__init__.py',
    f'{main_dir}/components/data_ingestion.py',
    f'{main_dir}/components/model_creation.py',
    f'{main_dir}/components/prepare_callback.py',
    f'{main_dir}/components/model_training.py',
    f'{main_dir}/components/model_evaluation.py',
    f'{main_dir}/utils/__init__.py',
    f'{main_dir}/pipeline/__init__.py',
    f'{main_dir}/pipeline/training_pipeline.py',
    f'{main_dir}/pipeline/prediction_pipeline.py',
    f'{main_dir}/entity/__init__.py',
    f'{main_dir}/constants/__init__.py',
    f'{main_dir}/config/__init__.py',
    "config/config.yaml",
    "YAML/dvc.yaml",
    "YAML/params.yaml",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    "research/notebook.ipynb",
    "templates/index.html",
    "static/style.css",
    "static/style.js"
]

for filpath in temp:
    filepath = Path(filpath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
