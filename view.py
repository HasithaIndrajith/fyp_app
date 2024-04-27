from flask import Flask, render_template,jsonify
import os
import subprocess


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/seq2vec')
def get_seq2vec_version():
    try:
        # Get seq2vec version
        result = subprocess.run(['seq2vec', '--help'], capture_output=True, text=True)
        output = result.stdout
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/kraken')
def get_kraken_version():
    try:
        working_directory = '/root/kraken'
        result = subprocess.run(['./kraken2'], capture_output=True, text=True, cwd=working_directory)
        if result.returncode == 0:
            output = result.stdout
            return jsonify({"output": output})
        else:
            error_message = result.stderr
            return jsonify({"error": error_message}), 500
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)