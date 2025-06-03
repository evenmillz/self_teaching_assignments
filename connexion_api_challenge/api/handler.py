import requests

def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json(), 200
    else:
        return {"error": "Post not found"}, response.status_code