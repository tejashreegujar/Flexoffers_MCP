from prefect import flow, task
from Program_Tool import ProgramTool
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

@task
def fetch_program(program_id: int):
    print(f"🔍 Fetching program {program_id}")

    api_key = os.getenv("FLEX_API_KEY")

    tool = ProgramTool(api_key)
    result = tool.get_program(program_id)

    print("✅ API Response:", result)
    return result


@flow
def run_program_flow(program_id: int = 127):
    return fetch_program(program_id)


if __name__ == "__main__":
    run_program_flow()