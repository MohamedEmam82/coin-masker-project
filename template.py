import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project = "CoinMasker"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    
    f"{project}/__init__.py",

    f"{project}/components/__init__.py",
    f"{project}/components/data_ingestion.py",
    f"{project}/components/data_validation.py",
    f"{project}/components/model_trainer.py",

    f"{project}/constant/__init__.py",
    f"{project}/constant/training_pipeline/__init__.py",
    f"{project}/constant/application.py",

    f"{project}/entity/config_entity.py",
    f"{project}/entity/artifacts_entity.py",

    f"{project}/exception/__init__.py",

    f"{project}/logger/__init__.py",

    f"{project}/pipeline/__init__.py",
    f"{project}/pipeline/training_pipeline.py",

    f"{project}/utils/__init__.py",
    f"{project}/utils/main_utils.py",

    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    
    else:
        logging.info(f"{filename} is already created")

