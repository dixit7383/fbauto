import facebook
import os
import requests
from datetime import datetime

# Load Facebook credentials from environment variables
FB_PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN")
FB_PAGE_ID = os.getenv("FB_PAGE_ID")

def post_to_facebook(message, image_path=None):
    """Post to Facebook Page with optional image"""
    try:
        graph = facebook.GraphAPI(FB_PAGE_TOKEN)
        
        if image_path:
            # Post with image
            if image_path.startswith(('http://', 'https://')):
                # Download remote image first
                local_image = "temp_image.jpg"
                with requests.get(image_path, stream=True) as r:
                    r.raise_for_status()
                    with open(local_image, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                image_to_post = local_image
            else:
                image_to_post = image_path
                
            with open(image_to_post, 'rb') as img:
                graph.put_photo(
                    image=img,
                    message=message,
                    album_path=f"{FB_PAGE_ID}/photos"
                )
            print(f"[{datetime.now()}] Successfully posted to Facebook with image!")
            
        else:
            # Text-only post
            graph.put_object(
                FB_PAGE_ID,
                "feed",
                message=message
            )
            print(f"[{datetime.now()}] Successfully posted text to Facebook!")
            
        return True
        
    except facebook.GraphAPIError as e:
        print(f"[{datetime.now()}] Facebook API Error: {str(e)}")
        return False
    except Exception as e:
        print(f"[{datetime.now()}] Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage
    post_text = "Automated post from Python script! 🚀\nPosted at: " + str(datetime.now())
    
    # Post text only
    post_to_facebook(post_text)
    
    # Post with image (uncomment to use)
    # post_to_facebook(
    #     message=post_text,
    #     image_path="https://example.com/image.jpg"  # or "local_image.jpg"
    # )
    
