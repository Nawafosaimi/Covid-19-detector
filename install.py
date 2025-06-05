import subprocess
import sys
import os
from pathlib import Path
import platform
import urllib.request
import joblib
import numpy as np
import cv2
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import glob

def download_and_prepare_data():
    print("\nPreparing training data...")
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Create directories for each class
    (data_dir / "COVID").mkdir(exist_ok=True)
    (data_dir / "Normal").mkdir(exist_ok=True)
    
    # Download sample images if they don't exist
    # Note: In a real application, you would download from a reliable source
    # For now, we'll use a small set of sample images
    sample_images = {
        "COVID": [
            "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/covid-19-pneumonia-16-PA.jpg",
            "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/covid-19-pneumonia-17-PA.jpg"
        ],
        "Normal": [
            "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/normal-1.jpg",
            "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/normal-2.jpg"
        ]
    }
    
    for class_name, urls in sample_images.items():
        for i, url in enumerate(urls):
            try:
                image_path = data_dir / class_name / f"{class_name.lower()}-{i}.jpg"
                if not image_path.exists():
                    print(f"Downloading {class_name} image {i+1}...")
                    urllib.request.urlretrieve(url, image_path)
            except Exception as e:
                print(f"Warning: Could not download {url}: {str(e)}")
                continue

def train_models():
    print("\nTraining models...")
    data_dir = Path("data")
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    # Load and preprocess images
    X = []
    y = []
    
    # Process COVID images
    for img_path in glob.glob(str(data_dir / "COVID" / "*.jpg")):
        try:
            img = cv2.imread(img_path, 0)  # Read as grayscale
            img = cv2.resize(img, (256, 256))
            X.append(img.reshape(-1))
            y.append(1)  # COVID class
        except Exception as e:
            print(f"Warning: Could not process {img_path}: {str(e)}")
    
    # Process Normal images
    for img_path in glob.glob(str(data_dir / "Normal" / "*.jpg")):
        try:
            img = cv2.imread(img_path, 0)  # Read as grayscale
            img = cv2.resize(img, (256, 256))
            X.append(img.reshape(-1))
            y.append(0)  # Normal class
        except Exception as e:
            print(f"Warning: Could not process {img_path}: {str(e)}")
    
    if not X or not y:
        print("Error: No training data available!")
        return
    
    X = np.array(X)
    y = np.array(y)
    
    # Train Random Forest model
    print("Training Random Forest model...")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    rf_model.fit(X, y)
    joblib.dump(rf_model, models_dir / "rf_model.joblib")
    
    # Train Neural Network model
    print("Training Neural Network model...")
    ann_model = MLPClassifier(
        hidden_layer_sizes=(100, 50),
        max_iter=1000,
        random_state=42
    )
    ann_model.fit(X, y)
    joblib.dump(ann_model, models_dir / "ann_model.joblib")
    
    print("Models trained successfully!")

def install_requirements():
    print("Installing required packages...")
    requirements = [
        "numpy>=1.21.0",
        "opencv-python>=4.5.3",
        "pillow>=9.0.0",
        "scikit-learn>=0.24.2",
        "joblib>=1.0.1",
        "matplotlib>=3.4.3",
        "seaborn>=0.11.2"
    ]
    
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_launcher():
    print("\nCreating launcher...")
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    
    # Create launcher based on platform
    system = platform.system()
    
    if system == "Windows":
        # Create Windows batch file
        launcher_path = current_dir / "COVID-19_Predictor.bat"
        launcher_content = f"""@echo off
cd /d "{current_dir}"
python covid.py
pause
"""
    else:
        # Create Unix-like shell script
        launcher_path = current_dir / "COVID-19_Predictor.command"
        launcher_content = f"""#!/bin/bash
cd "$(dirname "$0")"
python covid.py
"""
    
    # Write the launcher script
    with open(launcher_path, "w") as f:
        f.write(launcher_content)
    
    # Make it executable on Unix-like systems
    if system != "Windows":
        os.chmod(launcher_path, 0o755)
    
    print(f"\nInstallation complete! You can now run the application by:")
    if system == "Windows":
        print(f"1. Double-clicking 'COVID-19_Predictor.bat' in this folder")
    else:
        print(f"1. Double-clicking 'COVID-19_Predictor.command' in this folder")
    print(f"2. Or running 'python covid.py' from the terminal")

def main():
    print("COVID-19 X-ray Predictor Installation")
    print("=====================================")
    
    try:
        install_requirements()
        download_and_prepare_data()
        train_models()
        create_launcher()
    except Exception as e:
        print(f"\nError during installation: {str(e)}")
        print("Please contact technical support.")
        sys.exit(1)

if __name__ == "__main__":
    main() 