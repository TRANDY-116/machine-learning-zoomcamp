import pickle
import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()

model_file = 'model_C=1.0.bin'

# Load the model and vectorizer
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5
    result = {'churn_probability': float(y_pred), 'churn': bool(churn)}
    
    return jsonify(result)

        
if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '9696'))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    
    app.run(debug=debug, host=host, port=port)