import os
import json

def load_test_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "testdata", "testdata.json")

    with open(file_path) as file:
        return json.load(file)