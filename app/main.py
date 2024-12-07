from flask import Flask, request, render_template, jsonify
from llm_utils import summarize_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    input_text = data.get('text', '')
    if not input_text:
        return jsonify({"error": "No input text provided"}), 400

    try:
        summary = summarize_text(input_text)
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
