import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import joblib
import os
import sys

class COVIDPredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 X-ray Predictor")
        self.root.geometry("800x600")
        
        # Load models
        try:
            self.load_models()
            # Create GUI elements
            self.create_widgets()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize: {str(e)}")
            self.root.destroy()
            sys.exit(1)
        
    def load_models(self):
        try:
            self.rf_model = joblib.load('models/rf_model.joblib')
            self.ann_model = joblib.load('models/ann_model.joblib')
        except Exception as e:
            raise Exception(f"Could not load models: {str(e)}")
            
    def create_widgets(self):
        try:
            # Title
            title = tk.Label(self.root, text="COVID-19 X-ray Predictor", font=("Arial", 20))
            title.pack(pady=20)
            
            # Image selection button
            self.select_btn = tk.Button(self.root, text="Select X-ray Image", command=self.select_image)
            self.select_btn.pack(pady=10)
            
            # Image preview
            self.image_label = tk.Label(self.root)
            self.image_label.pack(pady=10)
            
            # Analysis buttons
            btn_frame = tk.Frame(self.root)
            btn_frame.pack(pady=20)
            
            self.quick_btn = tk.Button(btn_frame, text="Quick Scan (Random Forest)", 
                                     command=lambda: self.analyze_image('rf'))
            self.quick_btn.pack(side=tk.LEFT, padx=10)
            
            self.detailed_btn = tk.Button(btn_frame, text="Detailed Analysis (Neural Network)", 
                                        command=lambda: self.analyze_image('ann'))
            self.detailed_btn.pack(side=tk.LEFT, padx=10)
            
            # Results
            self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
            self.result_label.pack(pady=20)
        except Exception as e:
            raise Exception(f"Failed to create GUI: {str(e)}")
        
    def select_image(self):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg")]
            )
            if file_path:
                # Load and resize image for preview
                image = Image.open(file_path)
                image = image.resize((300, 300), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                
                self.image_label.configure(image=photo)
                self.image_label.image = photo
                
                # Store the original image path
                self.current_image_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
            
    def analyze_image(self, model_type):
        if not hasattr(self, 'current_image_path'):
            messagebox.showwarning("Warning", "Please select an image first!")
            return
            
        try:
            # Load and preprocess image
            image = cv2.imread(self.current_image_path, 0)
            image = cv2.resize(image, (256, 256))
            image = image.reshape(1, -1)
            
            # Make prediction
            if model_type == 'rf':
                model = self.rf_model
                model_name = "Random Forest"
            else:
                model = self.ann_model
                model_name = "Neural Network"
                
            prediction = model.predict(image)[0]
            confidence = model.predict_proba(image)[0][prediction] * 100
            
            result = f"Model: {model_name}\n"
            result += f"Prediction: {'COVID-19 Positive' if prediction == 1 else 'Normal'}\n"
            result += f"Confidence: {confidence:.2f}%"
            
            self.result_label.configure(text=result)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to analyze image: {str(e)}")

def main():
    try:
        root = tk.Tk()
        app = COVIDPredictor(root)
        root.mainloop()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

