import os
import requests
from datetime import datetime

def post_to_facebook():
    try:
        response = requests.post(
            f"https://graph.facebook.com/{os.getenv('PAGE_ID')}/feed",
            params={
                "message": "Automated post from GitHub",
                "access_token": os.getenv('FB_TOKEN')
            }
        )
        print(f"✅ Posted at {datetime.now()}")
    except Exception as e:
        print(f"❌ Failed: {str(e)}")

if __name__ == "__main__":
    post_to_facebook()
