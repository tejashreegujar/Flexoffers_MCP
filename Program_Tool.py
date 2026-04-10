import requests

class ProgramTool:
    def __init__(self, api_key):
        self.base_url = "http://iapi.dev.flexoffers.com/agents/v1/programs"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def get_program(self, program_id):
        url = f"{self.base_url}/{program_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()