from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"data": {
        "page": "Home",
        "message": "Welcome to the Website"
    }}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'data': {
        'id': id,
        'blog': 'Body of the blog'
    }}
