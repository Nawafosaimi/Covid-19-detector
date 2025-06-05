# COVID-19 X-ray Predictor

A machine learning tool for analyzing chest X-ray images to detect COVID-19. This application uses advanced machine learning models to provide accurate predictions while maintaining user privacy and ease of use.

## Key Features
- **Advanced Machine Learning Models**
  - Random Forest: Fast predictions for quick screening
  - Neural Network: High-accuracy analysis for detailed assessment
- **User-Friendly Interface**
  - Simple point-and-click operation
  - Real-time image analysis
  - Clear confidence scores
- **Privacy-Focused**
  - All processing done locally
  - No data sent to external servers
  - No internet connection required
- **Professional Grade**
  - Pre-trained models included
  - Comprehensive documentation
  - Regular updates and support

## Installation

### System Requirements
- macOS, Windows, or Linux
- Python 3.7 or higher
- 4GB RAM minimum
- 1GB free disk space

### Quick Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Nawafosaimi/COVID-19-Detector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd COVID-19-Detector
   ```
3. Run the installation script:
   ```bash
   python install.py
   ```

The installer will automatically:
- Set up a Python virtual environment
- Install required dependencies
- Configure the application

## Usage Guide

### Starting the Application
1. Run the launcher:
   ```bash
   python covid.py
   ```
2. Wait for the application window to appear

### Analyzing X-ray Images
1. **Select an Image**
   - Click "Select X-ray Image"
   - Choose any X-ray image (.png, .jpg, or .jpeg)
   - Preview the image in the window

2. **Choose Analysis Method**
   - **Quick Scan**: Uses Random Forest for fast results
   - **Detailed Analysis**: Uses Neural Network for higher accuracy

3. **View Results**
   - Prediction: COVID-19 Positive or Normal
   - Confidence Score: Percentage of certainty
   - Additional Analysis: Image quality assessment

## Project Structure
```
COVID-19-Predictor/
├── docs/                  # Documentation
│   └── USER_GUIDE.md     # Detailed user guide
├── models/               # Pre-trained models
│   ├── rf_model.joblib   # Random Forest model
│   └── ann_model.joblib  # Neural Network model
├── data/                 # Sample images
├── install.py           # Installation script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Machine Learning Details
- **Random Forest Model**
  - Fast inference time
  - Good for initial screening
  - Trained on 1000+ X-ray images
  - 85% accuracy on test set

- **Neural Network Model**
  - Higher accuracy predictions
  - Deep learning architecture
  - Trained on 2000+ X-ray images
  - 92% accuracy on test set

## Privacy and Security
- **Local Processing**: All analysis is performed on your computer
- **No Data Collection**: No images or results are stored or transmitted
- **Secure Models**: Pre-trained models are verified and optimized
- **Regular Updates**: Security patches and model improvements

## Support and Documentation
- **User Guide**: Complete documentation in `docs/USER_GUIDE.md`
- **Troubleshooting**: Common issues and solutions in the guide
- **Model Details**: Technical documentation in the user guide

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support, questions, or feedback:
- GitHub Issues: [Create an issue](https://github.com/Nawafosaimi/COVID-19-Detector/issues)

---

**Note**: This tool is designed to assist medical professionals and should not be used as a sole diagnostic tool. Always consult healthcare providers for medical decisions.
