import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_tkinter():
    try:
        import tkinter
        return True
    except ImportError:
        print("\nTkinter is not installed. Please install it using your system package manager:")
        print("\nFor macOS (using Homebrew):")
        print("brew install python-tk@3.12")
        print("\nFor Ubuntu/Debian:")
        print("sudo apt-get install python3-tk")
        print("\nFor Windows:")
        print("Tkinter should be included with Python installation")
        return False

def verify_installation():
    try:
        import numpy
        import sklearn
        import cv2
        import joblib
        import tqdm
        import matplotlib
        import seaborn
        print("\nVerification successful! All required packages are installed.")
        return True
    except ImportError as e:
        print(f"\nError: {str(e)}")
        print("Some packages were not installed correctly. Please try running the installation script again.")
        return False

def install_requirements():
    print("Installing required packages...")
    
    # First uninstall existing versions to avoid conflicts
    print("Removing existing packages...")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "numpy", "scikit-learn", "opencv-python", "joblib", "tqdm", "matplotlib", "seaborn"])
    
    # Install specific versions that match the training environment
    requirements = [
        "numpy==1.21.0",
        "opencv-python==4.5.3",
        "scikit-learn==0.24.2",
        "joblib==1.0.1",
        "tqdm==4.62.3",
        "matplotlib==3.4.3",
        "seaborn==0.11.2"
    ]
    
    print("\nInstalling packages...")
    for req in requirements:
        print(f"Installing {req}...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", req], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error installing {req}:")
            print(result.stderr)
            return False
    
    return verify_installation()

def copy_models():
    print("\nCopying trained models...")
    if not os.path.exists("models"):
        os.makedirs("models")
    
    # Copy models from the original training directory
    src_models = os.path.join("..", "COVID-19-Detection-Using-Chest-X-ray-Images", "models")
    if os.path.exists(src_models):
        for file in os.listdir(src_models):
            if file.endswith(".joblib"):
                shutil.copy2(os.path.join(src_models, file), os.path.join("models", file))
                print(f"Copied {file}")
    else:
        print("Warning: Could not find original models directory")

def create_launcher():
    print("\nCreating launcher file...")
    with open("run_covid_detector.command", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("cd \"$(dirname \"$0\")\"\n")
        f.write("python covid.py\n")
    
    os.chmod("run_covid_detector.command", 0o755)

def main():
    print("COVID-19 X-ray Predictor Installation")
    print("=====================================")
    
    if not check_tkinter():
        sys.exit(1)
    
    if not install_requirements():
        print("\nInstallation failed. Please try running the script again.")
        sys.exit(1)
    
    copy_models()
    create_launcher()
    
    print("\nInstallation completed successfully!")
    print("You can now run the application by double-clicking 'run_covid_detector.command'")

if __name__ == "__main__":
    main() 