"""
Diagnostic script to test MCP server configuration
"""
import json
import subprocess
import sys
from pathlib import Path

def test_mcp_server():
    """Test the MCP server configuration"""
    
    print("=== MCP Server Diagnostics ===\n")
    
    # 1. Check if uv is installed
    print("1. Checking if 'uv' is installed...")
    try:
        result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
        print(f"   ✓ uv version: {result.stdout.strip()}")
    except FileNotFoundError:
        print("   ✗ 'uv' not found in PATH")
        print("   → Install uv: https://github.com/astral-sh/uv")
        return
    
    # 2. Check if directory exists
    server_dir = r"C:\Users\jonat\Documents\koding\data-science-faggruppe-mcp-server-main"
    print(f"\n2. Checking if directory exists...")
    print(f"   Path: {server_dir}")
    dir_path = Path(server_dir)
    if dir_path.exists():
        print(f"   ✓ Directory exists")
    else:
        print(f"   ✗ Directory not found")
        return
    
    # 3. Check for required files
    print(f"\n3. Checking for required files...")
    files_to_check = ['main.py', 'server.py', 'services.py', 'pyproject.toml']
    for file in files_to_check:
        file_path = dir_path / file
        if file_path.exists():
            print(f"   ✓ {file}")
        else:
            print(f"   ✗ {file} not found")
    
    # 4. Try to run the server in inspection mode
    print(f"\n4. Testing server startup...")
    try:
        result = subprocess.run(
            ['uv', '--directory', server_dir, 'run', 'main.py'],
            capture_output=True,
            text=True,
            timeout=5,
            input='{"jsonrpc": "2.0", "method": "initialize", "params": {}, "id": 1}\n'
        )
        print(f"   stdout: {result.stdout[:200]}")
        print(f"   stderr: {result.stderr[:200]}")
    except subprocess.TimeoutExpired:
        print("   ⚠ Server started but didn't respond (this might be normal)")
    except Exception as e:
        print(f"   ✗ Error: {e}")
    
    # 5. Check Claude Desktop config
    print(f"\n5. Checking Claude Desktop config location...")
    config_paths = [
        Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json",
        Path.home() / ".config" / "claude" / "claude_desktop_config.json"
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            print(f"   ✓ Found config at: {config_path}")
            with open(config_path, 'r') as f:
                config = json.load(f)
                if 'mcpServers' in config:
                    print(f"   ✓ mcpServers found with {len(config['mcpServers'])} server(s)")
                    for server_name in config['mcpServers'].keys():
                        print(f"      - {server_name}")
        else:
            print(f"   ✗ Not found: {config_path}")

if __name__ == "__main__":
    test_mcp_server()