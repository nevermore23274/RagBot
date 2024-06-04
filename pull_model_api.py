from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/embeddings', methods=['POST'])
def embeddings():
    # Simulate an embedding response with the correct structure
    return jsonify({"embedding": [0.1, 0.2, 0.3]}), 200

@app.route('/pull_model', methods=['POST'])
def pull_model():
    model_name = request.json.get('model_name')
    if model_name:
        command = f"ollama pull {model_name}"
        os.system(command)
        return jsonify({"status": "success", "message": f"Model {model_name} pulled successfully"}), 200
    return jsonify({"status": "error", "message": "Model name is required"}), 400

@app.route('/models/<model_name>/generate', methods=['POST'])
def generate(model_name):
    prompt = request.json.get('prompt')
    if prompt:
        # Simulate a response from the model
        response = {
            "result": f"This is a response from the model: {model_name} for prompt: {prompt}"
        }
        return jsonify(response), 200
    return jsonify({"status": "error", "message": "Prompt is required"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11434)

