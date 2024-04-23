from flask import Flask, render_template,jsonify
import os
import subprocess


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seq2vec_version', methods=['GET'])
def get_seq2vec_version():
    try:
        # Get seq2vec version
        seq2vec_version = subprocess.check_output(['seq2vec', '--version']).decode().strip()
        return jsonify({"seq2vec_version": seq2vec_version})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)