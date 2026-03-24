<div align="center">

# TMDB MCP Server

**Give Claude superpowers over movies, TV shows, and more**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-1.20+-blueviolet?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/modelcontextprotocol/servers)
[![TMDB](https://img.shields.io/badge/TMDB-API%20v3-01D277?style=for-the-badge&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*A Model Context Protocol server that connects Claude AI to The Movie Database — search movies, discover trends, read reviews, and get recommendations through natural language.*

</div>

---

## Features

| Tool | Description |
|------|-------------|
| `tmdb_search_movies` | Search movies by title, year, region, and more |
| `tmdb_multi_search` | Search movies, TV shows, and people in one query |
| `tmdb_trending_search` | Get what's trending today or this week |
| `tmdb_movie_reviews` | Fetch user reviews for any movie |
| `tmdb_tv_reviews` | Fetch user reviews for any TV show |
| `tmdb_review_details` | Get full details on a specific review |
| `tmdb_tv_recommendations` | Get TV show recommendations |

---

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) — fast Python package manager
- A [TMDB API key](https://www.themoviedb.org/settings/api)

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure your API key

Get your bearer token from [TMDB API Settings](https://www.themoviedb.org/settings/api), then create a `.env` file:

```bash
TMDB_API_KEY="your_bearer_token_here"
```

![TMDB subscription screenshot](public/subscribe_screenshot.png)

### 3. Run the server

```bash
uv run main.py
```

You should see `Starting MCP server...` — you're live!

---

## Claude Desktop Integration

Add the server to your `claude_desktop_config.json`:

**macOS** (`~/Library/Application Support/Claude/claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "tmdb-server": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/mcp-mdtb-ai-pwc",
        "run",
        "main.py"
      ]
    }
  }
}
```

**Windows** (`%APPDATA%\Claude\claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "tmdb-server": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\ABSOLUTE\\PATH\\TO\\mcp-mdtb-ai-pwc",
        "run",
        "main.py"
      ]
    }
  }
}
```

> Replace the path with your own absolute path to this repo.

---

## Project Structure

```
mcp-mdtb-ai-pwc/
├── main.py          # Entry point — starts the MCP server
├── server.py        # MCP tool definitions
├── services.py      # TMDB API integration layer
├── .env             # Your API key (never committed)
└── pyproject.toml   # Project metadata and dependencies
```

---

## Development

- **TMDB API logic** lives in `services.py`
- **MCP tool definitions** live in `server.py`
- **Entry point** is `main.py`

Run the diagnostic script to verify your setup:

```bash
uv run test_mcp_config.py
```

---

## Notes

- This project is **not affiliated with TMDB**. You must provide your own API key.
- For more on MCP, see the [Model Context Protocol documentation](https://github.com/modelcontextprotocol/servers).

---

<div align="center">

Made with love, powered by [TMDB](https://www.themoviedb.org/) and [Claude](https://claude.ai)

</div>
