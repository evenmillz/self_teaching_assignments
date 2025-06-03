import requests

# URL for JSONPlaceholder posts
url = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request
response = requests.get(url)

# Check response status and print posts
if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:  # Show only the first 5 for brevity
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Failed to fetch posts. Status code: {response.status_code}")