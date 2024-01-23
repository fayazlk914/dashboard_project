from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for testing
sample_data = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Bob", "age": 22}
]

@app.route('/')
def home():
    return render_template('dashboard.html')

# API endpoint to fetch data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
