from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load and train the model at startup
df = pd.read_csv('sample_data.csv')
X = df.select_dtypes(include=[np.number])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = KMeans(n_clusters=3, random_state=42)
model.fit(X_scaled)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the request
        data = request.get_json()
        input_values = np.array([float(x) for x in data.values()]).reshape(1, -1)
        
        # Scale the input
        input_scaled = scaler.transform(input_values)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Get cluster center for more information
        cluster_center = model.cluster_centers_[prediction]
        
        return jsonify({
            'cluster': int(prediction),
            'cluster_center': cluster_center.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 