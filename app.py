from flask import Flask

stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": stores}
