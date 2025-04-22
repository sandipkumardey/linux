#!/bin/bash
# Display all files and directories in tree structure
tree() {
  for file in "$1"/*; do
    if [ -e "$file" ]; then
      printf "%*s- %s\n" $2 "" "$(basename "$file")"
      if [ -d "$file" ]; then
        tree "$file" $(( $2 + 2 ))
      fi
    fi
  done
}
tree . 0