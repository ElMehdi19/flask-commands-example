from app import app


@app.route('/')
def home():
    return {'message': 'Hello world'}
