from flask import Flask, request

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201
