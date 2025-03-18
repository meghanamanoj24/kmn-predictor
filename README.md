# K-means Clustering Predictor

This is a web application that allows you to train a K-means clustering model using your CSV dataset and make predictions through a user-friendly interface.

## Features

- Upload CSV dataset for training
- Train K-means clustering model
- Make predictions using trained model
- Modern and responsive web interface
- Real-time feedback on training and predictions

## Requirements

- Python 3.7+
- Flask
- Pandas
- Scikit-learn
- NumPy

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Follow the steps on the web interface:
   - Upload your CSV dataset
   - Train the model
   - Enter feature values to make predictions

## CSV Dataset Format

Your CSV file should contain numerical features. The application will automatically select all numerical columns for training. Make sure your CSV file:
- Has numerical values
- Has no missing values
- Has consistent data types

## Example CSV Format

```
feature1,feature2,feature3
1.2,3.4,5.6
2.3,4.5,6.7
3.4,5.6,7.8
```

## Notes

- The model uses 3 clusters by default
- Features are automatically scaled before training
- The application supports any number of numerical features 