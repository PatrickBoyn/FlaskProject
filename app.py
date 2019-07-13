from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "Acme Inc.",
        "items": [
            {
                "name": "barrels",
                "price": 30
            }
        ]
    }
]

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

# POST store items.
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass

# GET a store item.
@app.route('/store/<string:name>/item')
def get_item(name):
    pass

app.run(port=5500, debug=True)
