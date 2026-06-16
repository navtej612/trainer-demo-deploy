from mcp.server.fastmcp import FastMCP

mcp = FastMCP("trainer-demo-local-mcp")

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello {name}, your local MCP server is working!"

if __name__ == "__main__":
    mcp.run()