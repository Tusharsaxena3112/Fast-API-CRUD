from fastapi import FastAPI

app = FastAPI()


@app.get('/blogs')
def index(limit: int = 10, published: bool = True):
    if published:
        return {"data": {
            "page": f"{limit} Published Blogs",
        }}
    else:
        return {"data": {
            "page": f"{limit} All Blogs",
        }}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'data': {
        'id': id,
        'blog': 'Body of the blog'
    }}
