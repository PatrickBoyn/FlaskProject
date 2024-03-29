from flask import Flask, jsonify, request, render_template

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

@app.route('/')
def home():
    return render_template('index.html')

# Remember the s at the end of methods.
# POST a new store.
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)

# GET a single store.
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(name == store['name']):
            return jsonify(store)

    return jsonify({'message': 'No store found.'})

# GET all stores.
@app.route('/store')
def get_all_stores():
    return jsonify({'stores': stores})

# POST store items.
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):

    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'item not created.'})

# GET a store item.
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])

    return jsonify({'message': 'No item found'})


app.run(port=5500, debug=True)
