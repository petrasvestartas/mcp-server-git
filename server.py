from fastmcp import FastMCP

mcp = FastMCP("git")


@mcp.tool()
def pr() -> str:
    """Print the git PR shortcut commands."""
    snippet = (
        "gh repo clone <REPO>\n"
        "cd brg_framework\n"
        "gh pr checkout <BRANCH>"
    )
    return f"Reply with exactly this snippet and nothing else:\n\n```bash\n{snippet}\n```"


@mcp.tool()
def command(name: str = "") -> str:
    """List available commands."""
    if "pr" in name:
        return pr()

    return (
        "Reply with exactly this list, word for word. "
        "Do NOT call any other tools:\n\n"
        "- mcp_git_pr"
    )


if __name__ == "__main__":
    mcp.run()
