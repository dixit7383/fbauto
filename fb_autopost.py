import os
import requests
from datetime import datetime

def post_to_facebook():
    try:
        print("🔄 Attempting to post...")
        page_id = os.getenv('PAGE_ID')
        token = os.getenv('FB_TOKEN')
        
        print(f"ℹ️ Page ID: {page_id}")
        print(f"ℹ️ Token: {'*' * len(token[:-4]) + token[-4:]}" )  # Mask token
        
        response = requests.post(
            f"https://graph.facebook.com/{page_id}/feed",
            params={
                "message": f"Test post at {datetime.now()}",
                "access_token": token
            }
        )
        print(f"✅ Facebook response: {response.json()}")
        print("Posted successfully!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    post_to_facebook()
