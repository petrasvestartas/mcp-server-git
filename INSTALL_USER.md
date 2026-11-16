# User Installation (No Clone Needed)

Connect the MCP server directly using the git repository link.

## 1. Install GitHub CLI (`gh`)

- **Windows**: `winget install --id GitHub.cli`
- **macOS**: `brew install gh`
- **Ubuntu**: `sudo apt update && sudo apt install gh`

Authenticate: `gh auth login`

---

## 2. Connect Your LLM

Install [uv](https://docs.astral.sh/uv/) once.

### Via CLI

```bash
# Claude Code
claude mcp add --transport stdio --scope user git -- uvx --from git+https://github.com/petrasvestartas/mcp-server-git.git mcp-server-git

# Codex
codex mcp add git -- uvx --from git+https://github.com/petrasvestartas/mcp-server-git.git mcp-server-git

# Antigravity CLI
agy mcp add git uvx --from git+https://github.com/petrasvestartas/mcp-server-git.git mcp-server-git
```

### Via JSON Configuration (Claude Desktop, Cursor, Antigravity)

Add to your MCP config file:

```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/petrasvestartas/mcp-server-git.git",
        "mcp-server-git"
      ]
    }
  }
}
```

> **GUI app tip:** If Claude Desktop or Cursor says `command not found: uvx`, replace `"command": "uvx"` with its full path (`which uvx` on Linux/macOS, `where uvx` on Windows).

---

## Config File Locations

| App | Linux (Absolute) | macOS (Absolute) | Windows (Absolute) |
|---|---|---|---|
| **Antigravity** | `/home/<user>/.gemini/config/mcp_config.json` | `/Users/<user>/.gemini/config/mcp_config.json` | `C:\Users\<user>\.gemini\config\mcp_config.json` |
| **Claude Desktop** | `/home/<user>/.config/Claude/claude_desktop_config.json` | `/Users/<user>/Library/Application Support/Claude/claude_desktop_config.json` | `C:\Users\<user>\AppData\Roaming\Claude\claude_desktop_config.json` |
| **Cursor** | `/home/<user>/.cursor/mcp.json` | `/Users/<user>/.cursor/mcp.json` | `C:\Users\<user>\.cursor\mcp.json` |
| **Windsurf** | `/home/<user>/.codeium/windsurf/mcp_config.json` | `/Users/<user>/.codeium/windsurf/mcp_config.json` | `C:\Users\<user>\.codeium\windsurf\mcp_config.json` |
| **Claude Code** | `/home/<user>/.claude.json` | `/Users/<user>/.claude.json` | `C:\Users\<user>\.claude.json` |
