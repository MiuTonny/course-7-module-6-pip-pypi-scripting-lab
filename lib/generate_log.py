from datetime import datetime
import os
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    # TODO: Implement log generation logic
    # Validate input check if is a list
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:  # STEP 3: Write the log entries to a file using File I/O
        for entry in data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")# STEP 4: Print a confirmation message with the filename

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

