import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer  # Import the SimpleImputer

# Load data and handle missing values
data = pd.read_csv("Covid Data.csv")
data.replace({97: np.nan, 99: np.nan}, inplace=True)

# Encode categorical features
data['SEX'] = (data['SEX'] == 2).astype(int)
data['DIABETES'] = (data['DIABETES'] == 1).astype(int)
data['OBESITY'] = (data['OBESITY'] == 1).astype(int)
data['ASTHMA'] = (data['ASTHMA'] == 1).astype(int)
data['TOBACCO'] = (data['TOBACCO'] == 1).astype(int)

data['PATIENT_TYPE']= (data['PATIENT_TYPE'] == 1).astype(int)

    


# Select features and target variable
selected_columns = ['SEX', 'AGE', 'DIABETES', 'OBESITY', 'ASTHMA', 'TOBACCO','PATIENT_TYPE']
X = data[selected_columns]
y = (data['CLASIFFICATION_FINAL'] <= 3).astype(int)

# Handle missing values using imputation
imputer = SimpleImputer(strategy='mean')  # You can change the strategy as needed
X = imputer.fit_transform(X)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print the classification report
print(classification_report(y_test, y_pred))

