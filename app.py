from flask import Flask, jsonify, request

app = Flask(__name__)

# Remember the s at the end of methods.
# POST a new store.
@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass


app.run(port=5500, debug=True)
