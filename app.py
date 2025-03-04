import uuid

from flask import Flask, request

from db import items, stores

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values)}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, id: store_id}
    stores[store_id] = new_store
    return new_store, 201


app.post("/store/<string:name>/item")


def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item


@app.get("/store/<string:name>")
def get_store(store_id):
    try:
        # Here you might also want to add the items in this store
        # We'll do that later on in the course
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404


@app.get("/item/<string:item_id>")
def get_item_in_store(item_id):
    # for store in stores:
    #     if store["name"] == name:
    #         return {"items": store["items"]}
    # return {"message": "Store not found"}, 404
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}
