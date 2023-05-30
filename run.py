# run model student_tree.pkl

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
model = pickle.load(open('student_tree.pkl', 'rb'))
#new data = input
input_data = input().strip()

# Preprocess the input data
input_array = np.array(input_data.split(','), dtype=np.float64).reshape(1, -1)

# Make predictions using the machine learning model
predicted_value = model.predict(input_array)

# Print the predicted value to standard output
print(predicted_value)



