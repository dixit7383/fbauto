import facebook
import os

# Load token from GitHub Secrets
FB_PAGE_TOKEN = os.environ["FB_PAGE_TOKEN"]
FB_PAGE_ID = os.environ["FB_PAGE_ID"]

def post_to_facebook(message):
    graph = facebook.GraphAPI(FB_PAGE_TOKEN)
    graph.put_object(FB_PAGE_ID, "feed", message=message)
    print("Successfully posted to Facebook!")

if __name__ == "__main__":
    post_to_facebook("Hello from automated Python script! 🚀")
