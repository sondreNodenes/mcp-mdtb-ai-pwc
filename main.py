from dotenv import load_dotenv
from server import mcp


def main() -> None:
    mcp.run(transport="stdio")

if __name__ == "__main__":
    load_dotenv()
    print("Starting MCP server...")
    main()