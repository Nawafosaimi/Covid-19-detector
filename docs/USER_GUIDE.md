# COVID-19 X-ray Predictor - User Guide

## Quick Start
1. Double-click the `COVID-19_Predictor.command` file to start the application
2. Click "Select X-ray Image" to choose an X-ray image
3. Click "Predict" to see the results

## Detailed Instructions

### Starting the Application
- **Option 1**: Double-click `COVID-19_Predictor.command` in the folder
- **Option 2**: Open Terminal and run `python src/easy_predict.py`

### Using the Application
1. **Select an Image**
   - Click the "Select X-ray Image" button
   - Choose any X-ray image file (.png, .jpg, or .jpeg)
   - The image will be displayed in the window

2. **Choose Model Type**
   - **Random Forest (Fast)**: Quick predictions, good for initial screening
   - **Neural Network (Accurate)**: More detailed analysis, takes slightly longer

3. **Get Results**
   - Click the "Predict" button
   - The application will show:
     - Prediction: "COVID-19 Positive" or "Normal"
     - Confidence: How certain the model is about the prediction

### Understanding Results
- **Prediction**: Shows whether the X-ray indicates COVID-19 or normal condition
- **Confidence**: Shows how certain the model is (higher percentage = more certain)
- For best results, use clear, well-lit X-ray images

### Important Notes
- This tool is meant to assist in analysis, not replace professional judgment
- Always verify results with standard procedures
- Keep the application folder in its original location
- Do not delete any files from the folder

### Troubleshooting
If you encounter any issues:
1. Make sure all files are in their original locations
2. Try restarting the application
3. Contact technical support if problems persist

## Privacy and Security
- All image processing is done locally on your computer
- No images or data are sent to external servers
- You can safely use this tool with your data 