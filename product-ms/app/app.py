from flask import Flask, make_response, request, json, jsonify
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY = "This is an INSECURE secret!! DO NOT use this in production!",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@user_db/user',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
))

models.init_app(app)
models.create_table(app)

@app.route('/products/hello')
def hello():
    return 'Hello, welcome to the ESBay Product API\n'

@app.route('/api/product/create', methods=['POST'])
def post_create():

    name = request.form['name']
    seller = request.form['seller']
    price = request.form['price']

    item = models.Product()
    item.name = name
    item.seller = seller
    item.price = price

    models.db.session.add(item)
    models.db.session.commit()

    response = jsonify({'message': 'Product added', 'product': item.to_json()})

    return response

@app.route('/api/products', methods=['GET'])
def products():
    data = []

    for row in models.Product.query.all():
        data.append(row.to_json())

    response = jsonify({ 'results': data })

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)