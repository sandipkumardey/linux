#!/bin/bash

echo "Currently logged in user: $(whoami)"
echo "Your current shell: $SHELL"
echo "Your home directory: $HOME"
echo "Your operating system type: $(uname -o)"
echo "Your current path setting: $PATH"
echo "Your current working directory: $(pwd)"
echo "Number of users currently logged in: $(who | wc -l)"



