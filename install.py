import subprocess
import sys
import os
from pathlib import Path
import platform
import shutil

def copy_trained_models():
    print("\nCopying trained models...")
    # Source models directory (your trained models)
    source_dir = Path("../COVID-19-Detection-Using-Chest-X-ray-Images/models")
    # Destination models directory
    dest_dir = Path("models")
    dest_dir.mkdir(exist_ok=True)
    
    # Copy the models
    try:
        shutil.copy2(source_dir / "rf_model.joblib", dest_dir / "rf_model.joblib")
        shutil.copy2(source_dir / "ann_model.joblib", dest_dir / "ann_model.joblib")
        print("Models copied successfully!")
    except Exception as e:
        print(f"Error copying models: {str(e)}")
        print("Please make sure the trained models exist in the correct location.")
        sys.exit(1)

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
        copy_trained_models()
        create_launcher()
    except Exception as e:
        print(f"\nError during installation: {str(e)}")
        print("Please contact technical support.")
        sys.exit(1)

if __name__ == "__main__":
    main() 