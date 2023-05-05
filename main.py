from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/createposts")
def create_posts(payLoad:dict = Body(...)):
    print(payLoad)
    return {"new_post":f"title {payLoad['title']} ,content: {payLoad['content']}"}