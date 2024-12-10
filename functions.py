from dotenv import load_dotenv
import requests
import os

def load_data(day):
    load_dotenv()
    link = f"https://adventofcode.com/2024/day/{day}/input"
    SESSION_ID = os.environ.get("SESSION_ID")
    data = requests.get(link, cookies={'session': SESSION_ID})
    return data.text