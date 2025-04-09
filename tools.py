import helpers
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("search")


@mcp.tool()
def search(query: str) -> str:
    """根据 query 发起互联网搜索最新的结果

    Args:
        query: 一段自然语言描述的查询
    """
    return helpers.search(query)
