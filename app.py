from flask import Flask, jsonify, request

app = Flask(__name__)

# Remember the s at the end of methods.
# POST a new store.
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET a single store.
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET all stores.
@app.route('/store')
def get_stores():
    pass

# Create store items.
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass

app.run(port=5500, debug=True)
