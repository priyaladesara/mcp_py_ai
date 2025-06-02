from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE=os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE , "w") as f:
            f.write("")

# creating various mcp tool under our mcp server
@mcp.tool()
def add_note(message: str) -> str:
    """
    Appends a note to the notes file.

    Args:
        message(str) : The note content to be added.

    Return:
      str: A confirmation message indicating the note was saved.
    """
    ensure_file()  # ensure that the storage file exists
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.

    Returns:
        str: All notes as a single string separated by line breaks.
             If no notes are present, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No notes available."

# creating resources - get operations based mostly
@mcp.resource("notes://latest")
def get_latest_note() -> str:
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def note_Summary_prompt() -> str:
    """
    Retrieve the latest note from the sticky notes file.

    Returns:
        str: The most recently added note, with leading/trailing whitespace removed.
             If no notes are present, returns "No notes yet."
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes yet"
    return f"summarize this current notes : {content}"


