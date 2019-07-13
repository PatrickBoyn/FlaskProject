from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Test store 1',
        'items': [
            {
                'name': 'apples',
                'price': 3.45,
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    
    stores.append(new_store)
    
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)

    return jsonify({'message': 'Store not found.'})
            

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    pass

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({store['items']})

    return jsonify({'message': 'Item not found.'})

app.run(port=5500, debug=True)