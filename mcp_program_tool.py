from mcp.server.fastmcp import FastMCP
from Program_Tool import ProgramTool
from dotenv import load_dotenv
import os
mcp = FastMCP("program-service")
load_dotenv()  # loads .env file
API_KEY = os.getenv("FLEX_API_KEY")

tool = ProgramTool(API_KEY)

@mcp.tool()
async def get_program(program_id: int):
    """
    Fetch program details using program ID
    """
    print(f"📞 Fetching program: {program_id}")
    return await tool.get_program(program_id)

if __name__ == "__main__":
    print("✅ MCP running... waiting for requests")
    mcp.run()