import os
import requests
from datetime import datetime

def post_to_facebook():
    try:
        # First verify page access
        page_info = requests.get(
            f"https://graph.facebook.com/{os.getenv('PAGE_ID')}",
            params={
                'access_token': os.getenv('FB_TOKEN'),
                'fields': 'name'
            }
        ).json()
        print("PAGE VERIFICATION:", page_info)

        # Then make the post
        response = requests.post(
            f"https://graph.facebook.com/{os.getenv('PAGE_ID')}/feed",
            params={
                "message": f"Test post at {datetime.now()}",
                "access_token": os.getenv('FB_TOKEN')
            }
        )
        print("✅ POSTED! Response:", response.json())
        
    except Exception as e:
        print("❌ FAILED:", str(e))

if __name__ == "__main__":
    post_to_facebook()
