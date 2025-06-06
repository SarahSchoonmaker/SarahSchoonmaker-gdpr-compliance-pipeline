import os
from dotenv import load_dotenv
import kagglehub
import pandas as pd

# Load Kaggle credentials
load_dotenv()

os.environ["KAGGLE_USERNAME"] = os.getenv("KAGGLE_USERNAME")
os.environ["KAGGLE_KEY"] = os.getenv("KAGGLE_KEY")

# Download dataset
print("Downloading GDPR violations dataset...")
path = kagglehub.dataset_download("jessemostipak/gdpr-violations")
print("Dataset downloaded to:", path)

# Load and preview
csv_path = os.path.join(path, "gdpr_violations.csv")
df = pd.read_csv(csv_path)
print(df.head())
