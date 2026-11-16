# Developer Installation (Local Use Only)

For developing, testing, and modifying `server.py` directly on your local machine.

## 1. Setup Local Environment

Install [uv](https://docs.astral.sh/uv/) once. Inside the local folder:

```bash
uv venv
uv pip install fastmcp
```

---

## 2. Test Locally

Run the server directly in your terminal to verify it starts without errors:

```bash
uv run python server.py
```

---

## 3. Connect to LLM (Using Local Directory Path)

Replace `/path/to/mcp-server-git` with the absolute path of this local folder (e.g. `/home/pv/brg/code_python/mcp-server-git`).

### Via CLI

```bash
# Claude Code
claude mcp add --transport stdio --scope user git -- uv --directory /path/to/mcp-server-git run --with fastmcp python server.py

# Antigravity CLI
agy mcp add git uv --directory /path/to/mcp-server-git run --with fastmcp python server.py
```

### Via JSON Configuration

Add to your local MCP configuration file:

```json
{
  "mcpServers": {
    "git": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-git",
        "run",
        "--with",
        "fastmcp",
        "python",
        "server.py"
      ]
    }
  }
}
```
