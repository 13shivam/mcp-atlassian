"""I/O utility functions for MCP Atlassian."""

from mcp_atlassian.utils.env import is_env_extended_truthy


def is_read_only_mode() -> bool:
    """Check if the server is running in read-only mode.

    This MCP server is permanently configured as read-only.
    All write operations (create, update, delete) are disabled.
    Only read operations are allowed.

    Returns:
        Always returns True - this server is read-only only
    """
    return True
