from flask import Flask, jsonify, request

# Simple Flask app for Azure deployment
app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/compute', methods=['POST'])
def compute():
    data = request.get_json(silent=True) or {}
    a = data.get('a', 0)
    b = data.get('b', 0)
    try:
        result = float(a) + float(b)
    except Exception:
        return jsonify({"error": "Invalid numbers"}), 400
    return jsonify({"a": a, "b": b, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
