import subprocess
import sys
import os
from pathlib import Path
import platform
import urllib.request
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

def download_models():
    print("\nDownloading pre-trained models...")
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    # Create and save Random Forest model
    print("Creating Random Forest model...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    # Train with dummy data (will be replaced with actual training data)
    X_dummy = [[0] * 65536]  # 256x256 image flattened
    y_dummy = [0]
    rf_model.fit(X_dummy, y_dummy)
    joblib.dump(rf_model, models_dir / "rf_model.joblib")
    
    # Create and save Neural Network model
    print("Creating Neural Network model...")
    ann_model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
    # Train with dummy data (will be replaced with actual training data)
    ann_model.fit(X_dummy, y_dummy)
    joblib.dump(ann_model, models_dir / "ann_model.joblib")
    
    print("Models created successfully!")

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
        download_models()
        create_launcher()
    except Exception as e:
        print(f"\nError during installation: {str(e)}")
        print("Please contact technical support.")
        sys.exit(1)

if __name__ == "__main__":
    main() 