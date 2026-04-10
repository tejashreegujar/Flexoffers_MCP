from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

app = FastAPI(title="Simple MCP Tool")

# Load environment variables
load_dotenv()
API_KEY = os.getenv("FLEX_API_KEY")


# -----------------------------
# Request Model
# -----------------------------
class ProgramRequest(BaseModel):
    program_id: int


# -----------------------------
# Tool Class
# -----------------------------
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


# Initialize tool
tool = ProgramTool(API_KEY)


# -----------------------------
# MCP-style Endpoint
# -----------------------------
@app.post("/tools/get_program")
def get_program_endpoint(request: ProgramRequest):
    result = tool.get_program(request.program_id)

    return {
        "tool": "get_program",
        "input": request.dict(),
        "output": result,
        "status": "success"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def root():
    return {"message": "MCP Tool Running"}