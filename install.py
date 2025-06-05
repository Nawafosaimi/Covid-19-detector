import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    print("Installing required packages...")
    requirements = [
        "numpy",
        "opencv-python",
        "pillow",
        "scikit-learn",
        "joblib",
        "matplotlib",
        "seaborn"
    ]
    
    for package in requirements:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def create_desktop_shortcut():
    print("\nCreating desktop shortcut...")
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    
    # Create a simple launcher script
    launcher_content = f"""#!/bin/bash
cd "{current_dir}"
python src/easy_predict.py
"""
    
    # Write the launcher script
    launcher_path = current_dir / "COVID-19_Predictor.command"
    with open(launcher_path, "w") as f:
        f.write(launcher_content)
    
    # Make it executable
    os.chmod(launcher_path, 0o755)
    
    print(f"\nInstallation complete! You can now run the application by:")
    print(f"1. Double-clicking 'COVID-19_Predictor.command' in this folder")
    print(f"2. Or running 'python src/easy_predict.py' from the terminal")

def main():
    print("COVID-19 X-ray Predictor Installation")
    print("=====================================")
    
    try:
        install_requirements()
        create_desktop_shortcut()
    except Exception as e:
        print(f"\nError during installation: {str(e)}")
        print("Please contact technical support.")
        sys.exit(1)

if __name__ == "__main__":
    main() 