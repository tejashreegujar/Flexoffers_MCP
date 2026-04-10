from mcp.server.fastmcp import FastMCP
from Program_Tool import ProgramTool
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
API_KEY = os.getenv("FLEX_API_KEY")

mcp = FastMCP("program-service")
tool = ProgramTool(API_KEY)

@mcp.tool()
async def get_program(program_id: int):
    return await tool.get_program(program_id)

async def main():
    print("✅ MCP running... waiting for requests")
    await mcp.run_async()

if __name__ == "__main__":
    asyncio.run(main())