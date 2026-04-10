from mcp.server.fastmcp import FastMCP
from Program_Tool import ProgramTool
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("FLEX_API_KEY")

mcp = FastMCP("program-service")
tool = ProgramTool(API_KEY)

@mcp.tool()
async def get_program(program_id: int):
    return await tool.get_program(program_id)

if __name__ == "__main__":
    print("✅ MCP running... waiting for requests")
    mcp.run(transport="sse")  # for HTTP/SSE on the configured port