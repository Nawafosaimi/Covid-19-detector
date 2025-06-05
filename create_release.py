import shutil
from pathlib import Path
import os
import sys
from tqdm import tqdm

def create_distribution():
    print("Creating distribution package...")
    
    # Get the project root directory
    root_dir = Path(__file__).parent
    
    # Create dist directory
    dist_dir = root_dir / 'dist'
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(exist_ok=True)
    
    # Create the distribution structure
    app_dir = dist_dir / 'COVID-19-Predictor'
    if app_dir.exists():
        shutil.rmtree(app_dir)
    app_dir.mkdir(exist_ok=True)
    
    # Create necessary directories
    (app_dir / 'src').mkdir(exist_ok=True)
    (app_dir / 'models').mkdir(exist_ok=True)
    (app_dir / 'docs').mkdir(exist_ok=True)
    
    # Files to copy
    files_to_copy = [
        ('src/easy_predict.py', 'src/'),
        ('src/data_processor.py', 'src/'),
        ('models/rf_model.joblib', 'models/'),
        ('models/ann_model.joblib', 'models/'),
        ('docs/USER_GUIDE.md', 'docs/'),
        ('install.py', '.'),
        ('README.md', '.'),
        ('LICENSE', '.'),
        ('requirements.txt', '.')
    ]
    
    # Copy files with progress bar
    for src, dest in tqdm(files_to_copy, desc="Copying files"):
        src_path = root_dir / src
        dest_path = app_dir / dest / src_path.name
        
        if src_path.is_file():
            shutil.copy2(src_path, dest_path)
    
    # Create launcher with correct path and dependency installation
    launcher_content = """#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 from https://www.python.org/downloads/"
    read -p "Press Enter to exit..."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Run the application
python3 src/easy_predict.py

# Keep the window open if there's an error
if [ $? -ne 0 ]; then
    echo "An error occurred. Please check the messages above."
    read -p "Press Enter to exit..."
fi
"""
    
    launcher_path = app_dir / 'COVID-19_Predictor.command'
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    os.chmod(launcher_path, 0o755)
    
    # Create zip
    print("\nCreating ZIP file...")
    shutil.make_archive(str(dist_dir / 'COVID-19-Predictor'), 'zip', dist_dir, 'COVID-19-Predictor')
    
    # Clean up
    shutil.rmtree(app_dir)
    
    print("\nDistribution package created successfully!")
    print(f"Location: {dist_dir}/COVID-19-Predictor.zip")
    print("\nTo use:")
    print("1. Extract the ZIP file")
    print("2. Double-click COVID-19_Predictor.command")
    print("3. Wait for the dependencies to install")
    print("4. If you get a security warning, right-click and select 'Open'")

if __name__ == "__main__":
    create_distribution() 