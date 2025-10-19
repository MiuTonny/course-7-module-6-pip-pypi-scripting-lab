from datetime import datetime
import os
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    # STEP 1: Validate input (must be a list)
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write entries to the file (creates empty file if data == [])
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation and RETURN the filename for tests
    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}"
    ]
    generate_log(log_data)

