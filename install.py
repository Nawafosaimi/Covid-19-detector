import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox
import venv
import platform

def check_tkinter():
    try:
        import tkinter
        return True
    except ImportError:
        print("\nTkinter is not installed. Please install it using your system package manager:")
        print("\nFor macOS (using Homebrew):")
        print("brew install python-tk@3.9")
        print("\nFor Ubuntu/Debian:")
        print("sudo apt-get install python3-tk")
        print("\nFor Windows:")
        print("Tkinter should be included with Python installation")
        return False

def create_venv():
    print("\nCreating Python 3.9 virtual environment...")
    venv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv")
    
    # Check if Python 3.9 is installed
    try:
        subprocess.run(["python3.9", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nPython 3.9 is not installed. Please install it first:")
        if platform.system() == "Darwin":  # macOS
            print("brew install python@3.9")
        elif platform.system() == "Linux":
            print("sudo apt-get install python3.9 python3.9-venv")
        elif platform.system() == "Windows":
            print("Download and install Python 3.9 from https://www.python.org/downloads/")
        sys.exit(1)
    
    # Create virtual environment
    venv.create(venv_path, with_pip=True)
    
    # Get the path to the Python executable in the virtual environment
    if platform.system() == "Windows":
        python_path = os.path.join(venv_path, "Scripts", "python.exe")
    else:
        python_path = os.path.join(venv_path, "bin", "python")
    
    return python_path

def verify_installation(python_path):
    try:
        result = subprocess.run([python_path, "-c", """
import numpy
import sklearn
import cv2
import joblib
import tqdm
import matplotlib
import seaborn
print("Verification successful!")
"""], capture_output=True, text=True)
        if "Verification successful!" in result.stdout:
            print("\nVerification successful! All required packages are installed.")
            return True
        else:
            print("\nVerification failed. Some packages are not installed correctly.")
            return False
    except Exception as e:
        print(f"\nError during verification: {str(e)}")
        return False

def install_requirements(python_path):
    print("Installing required packages...")
    
    # Install packages in a specific order with exact versions
    print("\nInstalling packages...")
    packages = [
        "numpy==1.21.0",
        "scipy==1.7.0",
        "scikit-learn==0.24.2",
        "opencv-python==4.5.3",
        "joblib==1.0.1",
        "tqdm==4.62.3",
        "matplotlib==3.4.3",
        "seaborn==0.11.2"
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        result = subprocess.run([python_path, "-m", "pip", "install", package], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error installing {package}:")
            print(result.stderr)
            return False
    
    return verify_installation(python_path)

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

def create_launcher(python_path):
    print("\nCreating launcher file...")
    if platform.system() == "Windows":
        launcher_path = "run_covid_detector.bat"
        with open(launcher_path, "w") as f:
            f.write(f"@echo off\n")
            f.write(f"cd /d \"%~dp0\"\n")
            f.write(f"\"{python_path}\" covid.py\n")
            f.write("pause\n")
    else:
        launcher_path = "run_covid_detector.command"
        with open(launcher_path, "w") as f:
            f.write("#!/bin/bash\n")
            f.write("cd \"$(dirname \"$0\")\"\n")
            f.write(f"\"{python_path}\" covid.py\n")
        os.chmod(launcher_path, 0o755)

def main():
    print("COVID-19 X-ray Predictor Installation")
    print("=====================================")
    
    if not check_tkinter():
        sys.exit(1)
    
    python_path = create_venv()
    
    if not install_requirements(python_path):
        print("\nInstallation failed. Please try running the script again.")
        sys.exit(1)
    
    copy_models()
    create_launcher(python_path)
    
    print("\nInstallation completed successfully!")
    print("You can now run the application by double-clicking 'run_covid_detector.command'")

if __name__ == "__main__":
    main() 