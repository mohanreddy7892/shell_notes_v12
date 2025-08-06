#!/usr/bin/env bash
# A small utility script to copy files or directories from one server to another.
#
# Usage:
#   ./copy_between_servers.sh <source> <destination>
#
# Example:
#   ./copy_between_servers.sh user1@server1:/path/to/file user2@server2:/path/to/dir/
#
# The script simply wraps the scp command with recursive option enabled so it
# can handle directories as well as single files.

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <source> <destination>" >&2
  exit 1
fi

scp -r "$1" "$2"
