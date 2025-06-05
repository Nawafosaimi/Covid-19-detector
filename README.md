# COVID-19 X-ray Predictor

<<<<<<< HEAD
A machine learning tool for analyzing chest X-ray images to detect COVID-19. This project uses both Random Forest and Neural Network models to provide accurate predictions.

## Features
- Simple graphical user interface
- Two model options:
  - Random Forest (Fast predictions)
  - Neural Network (More accurate)
- Real-time image analysis
- Confidence scores for predictions
- No internet connection required
- Privacy-focused (all processing done locally)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Download the latest release from the releases page
2. Extract the ZIP file
3. Double-click `Start_Predictor.command` to begin installation

The installer will:
- Install all required packages
- Set up the application
- Create necessary directories

## Usage

### Quick Start
1. Double-click `Start_Predictor.command` to start the application
2. Click "Select X-ray Image" to choose an X-ray image
3. Click "Predict" to see the results

### Detailed Usage
1. **Selecting an Image**
   - Click "Select X-ray Image"
   - Choose any X-ray image (.png, .jpg, or .jpeg)
   - The image will be displayed in the window

2. **Choosing a Model**
   - **Random Forest (Fast)**: Quick predictions, good for initial screening
   - **Neural Network (Accurate)**: More detailed analysis, takes slightly longer

3. **Getting Results**
   - Click "Predict"
   - View the prediction (COVID-19 Positive or Normal)
   - Check the confidence level

## Project Structure
```
COVID-19-Predictor/
├── docs/                  # Documentation
│   └── USER_GUIDE.md     # User guide
├── models/               # Trained models
├── src/                  # Application files
├── Start_Predictor.command  # Launcher
└── README.md           # This file
```

## Privacy and Security
- All processing is done locally on your computer
- No data is sent to external servers
- Models are pre-trained and included in the package
- Source code is protected

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For issues and questions, please:
1. Check the documentation in `docs/USER_GUIDE.md`
2. Contact the maintainers
=======
A tool for analyzing chest X-ray images to detect COVID-19.

## Project Structure
- `docs/`: Documentation and guides
- `models/`: Trained machine learning models
- `src/`: Source code
- `evaluation_results/`: Model performance metrics
- `data/`: Dataset and sample images

## Quick Start
1. Run `python install.py` to set up the application
2. Double-click `COVID-19_Predictor.command` to start
3. Follow the instructions in `docs/USER_GUIDE.md`

## Contents
- `docs/USER_GUIDE.md`: Complete user guide
- `src/easy_predict.py`: Main application
- `models/`: Contains trained models
- `data/`: Sample X-ray images

## Support
For any issues, please refer to the user guide in the `docs` folder.
>>>>>>> 1b73d544 (Initial commit: COVID-19 Detector Source Code)
