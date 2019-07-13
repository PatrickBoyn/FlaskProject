from flask import Flask, jsonify, request

app = Flask(__name__)

# Remember the s at the end of methods.
@app.route('/store', methods=['POST'])
def create_store():
    pass

app.run(port=5500, debug=True)
