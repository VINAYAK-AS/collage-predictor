from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = pickle.load(open('model/college_model.pkl', 'rb'))

# Load encoder (for category / course if needed)
encoder = pickle.load(open('model/encoder.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        rank = int(request.form['rank'])
        category = request.form['category']
        course = request.form['course']

        # Encode categorical values
        encoded_features = encoder.transform([[category, course]])

        # Combine rank with encoded values
        final_input = np.hstack(([[rank]], encoded_features))

        # Predict
        prediction = model.predict(final_input)
        probability = model.predict_proba(final_input)

        return render_template(
            'result.html',
            college=prediction[0],
            confidence=round(max(probability[0]) * 100, 2)
        )

    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
