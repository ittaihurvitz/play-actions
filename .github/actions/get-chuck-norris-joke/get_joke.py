import os
import requests
import json

def main():
    url = os.getenv('INPUT_URL')
    response = requests.get(url)
    joke = response.json().get('value')

    print(f"::set-output name=joke::{joke}")

if __name__ == "__main__":
    main()
