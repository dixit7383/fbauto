import os
import requests
from datetime import datetime

def post_to_facebook():
    try:
        # Get credentials
        token = os.getenv('FB_TOKEN')
        page_id = os.getenv('PAGE_ID')
        
        # Make the post
        response = requests.post(
            f"https://graph.facebook.com/{page_id}/feed",
            params={
                "message": f"Test post at {datetime.now()}",
                "access_token": token
            }
        )
        print("✅ POSTED! Facebook response:", response.json())
    except Exception as e:
        print("❌ FAILED:", str(e))

if __name__ == "__main__":
    post_to_facebook()
