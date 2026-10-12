from fastapi import FastAPI, HTTPException
from app.schema import PostCreate

# Application Init 
app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Morning Thoughts", "content": "Today is a beautiful day to code."},
    3: {"title": "FastAPI Tips", "content": "FastAPI is fast and easy to use."},
    4: {"title": "Python News", "content": "Python 3.12 introduces great improvements."},
    5: {"title": "Learning Backend", "content": "APIs are essential for modern applications."},
    6: {"title": "Coffee Break", "content": "Nothing beats coffee while debugging."},
    7: {"title": "Dev Journal", "content": "Worked on authentication today."},
    8: {"title": "Weekend Project", "content": "Building a blog API with FastAPI."},
    9: {"title": "Testing API", "content": "Always test your endpoints carefully."},
    10: {"title": "Docker Setup", "content": "Containers simplify deployment."},
    11: {"title": "Final Note", "content": "Consistency is key in programming."}
}

@app.get("/posts")
def get_all_post(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts [max(text_posts. keys()) + 1] = {"title": post.title, "content": post.content}
    return new_post