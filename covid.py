import numpy as np
import cv2
import glob
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score

# Step 1: Data Preprocessing
X = []
y = []

# Processing first class
for file in glob.glob('/Users/unknown/Desktop/covid/COVID-19_Radiography_Dataset/Normal/images/*.png'):
    images = cv2.imread(file, 0)
    Resize_image = cv2.resize(images, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
    Reshape_image = Resize_image.reshape(1, 256 * 256)
    X.append(Reshape_image)
    y.append(0)

# Processing second class
for file in glob.glob('/Users/unknown/Desktop/covid/COVID-19_Radiography_Dataset/COVID/images/*.png'):
    images = cv2.imread(file, 0)
    Resize_image = cv2.resize(images, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
    Reshape_image = Resize_image.reshape(1, 256 * 256)
    X.append(Reshape_image)
    y.append(1)

X = np.array(X)
X = X.reshape(X.shape[0], 256 * 256)

y = np.array(y)
y = y.reshape(y.shape[0], 1)

# Step 2: Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Using an Artificial Neural Network
clf_ann = MLPClassifier(solver='adam', hidden_layer_sizes=(5, 2))
clf_ann.fit(X_train, y_train)

# Using a Random Forest Classifier
clf_rf = RandomForestClassifier()
clf_rf.fit(X_train, y_train)

# Step 3: Model Evaluation
Model_pred_test_ann = clf_ann.predict(X_test)
Model_pred_test_rf = clf_rf.predict(X_test)

print('ANN Test Accuracy Score:', accuracy_score(y_test, Model_pred_test_ann))
print('ANN Test Precision Score:', precision_score(y_test, Model_pred_test_ann, average='weighted'))
print('ANN Test Recall Score:', recall_score(y_test, Model_pred_test_ann, average='weighted'))

print('RF Test Accuracy Score:', accuracy_score(y_test, Model_pred_test_rf))
print('RF Test Precision Score:', precision_score(y_test, Model_pred_test_rf, average='weighted'))
print('RF Test Recall Score:', recall_score(y_test, Model_pred_test_rf, average='weighted'))

