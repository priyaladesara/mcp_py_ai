# 🗒️ AI Sticky Notes —  Custom MCP Server 

This project is a simple **MCP (Model Context Protocol)** server that demonstrates how to expose tools, resources, and prompts for an AI agent (like **Claude Desktop**) to call.

It shows how to create a custom **Sticky Notes server** where notes are added, read, or summarized through an MCP-compatible client.


## 📌 What is MCP?

**MCP** stands for **Model Context Protocol** — a standard for defining **tools**, **resources**, and **prompts** that an AI model can call dynamically at runtime.

In this project:
- The **MCP Server** is defined with [`FastMCP`](https://github.com/openai/mcp) (or your custom implementation)
- The **Client** is **Claude Desktop**, which calls your server’s tools via the MCP protocol



## ✅ What does this project do?

- **Add Notes:** Save sticky notes to a local text file
- **Read Notes:** Return all saved notes
- **Get Latest Note:** Return only the most recent note
- **Summarize Notes:** Generate a prompt for the AI to summarize the notes

Everything is saved in a simple `notes.txt` file next to your server script.


## ⚙️ How does it work?

| Decorator | Purpose | Example |
|-----------|---------|---------|
| `@mcp.tool()` | Defines a **tool** (action) the AI can call | `add_note()`, `read_notes()` |
| `@mcp.resource()` | Defines a **resource** (read-only endpoint) | `get_latest_note()` |
| `@mcp.prompt()` | Defines a **prompt template** | `note_Summary_prompt()` |

## 📌 How to Set Claude Desktop as Client and Add Your MCP Server

Follow these steps to make Claude Desktop use your custom MCP server as a local tool:

### 1️. Install & Open Claude Desktop

1. Download and install [Claude Desktop](https://www.anthropic.com).
2. Open Claude Desktop and make sure it’s working.

### 2️ Locate Claude Desktop Config Folder

On **Windows**, the config folder is usually:

```bash
C:\Users\<YOUR_USERNAME>\AppData\Roaming\Claude
```
On macOS, it’s usually:
```bash
~/Library/Application Support/Claude
```

### 3. Create or Edit .claude-tools.json

```bash
.claude-tools.json
```

### 4.Add Your MCP Server Configuration

```bash
{
  "tools": [
    {
      "name": "StickyNotesServer",
      "type": "mcp",
      "mcp": {
        "url": "http://localhost:8000",
        "headers": {}
      }
    }
  ]
}

```

## Quick Start

### 1.Clone the Repository

```bash
git clone https://github.com/your-org/ai-sticky-notes.git
cd ai-sticky-notes
```

### 2.Adding MCP to your python project

 create a uv-managed project :

   ```bash
   uv init mcp-server-demo
   cd mcp-server-demo
   ```

Then add MCP to your project dependencies:

   ```bash
   uv add "mcp[cli]"
   ```

Alternatively, for projects using pip for dependencies:
```bash
pip install "mcp[cli]"
```

### 3. Example Usage
In Claude Desktop, you can run:

- “Add a note: Buy groceries tomorrow”
- “Read all sticky notes”
- “What’s my latest note?”
- “Summarize my notes”


## 📽️ Demo Video

- link to be attackh




