import os
import requests
from datetime import datetime

def post_to_facebook(message):
    try:
        response = requests.post(
            f"https://graph.facebook.com/{os.getenv('PAGE_ID')}/feed",
            params={
                "message": message,
                "access_token": os.getenv('FB_ACCESS_TOKEN')
            }
        )
        response.raise_for_status()
        print(f"✅ Posted successfully at {datetime.now()}")
    except Exception as e:
        print(f"❌ Failed to post: {str(e)}")
        # Uncomment to add error notifications later:
        # send_error_alert(str(e))

if __name__ == "__main__":
    post_to_facebook("Automated post from GitHub Actions")
