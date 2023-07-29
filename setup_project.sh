#!/bin/bash

# Script to set up a Python project from scratch

# Function to check if ffmpeg is installed
check_ffmpeg_installed() {
    if dpkg-query -W -f='${Status}' ffmpeg 2>/dev/null | grep -q "installed"; then
        return 0
    else
        return 1
    fi
}

# Check if ffmpeg is installed
if check_ffmpeg_installed; then
    echo "ffmpeg is already installed."
else
    echo "ffmpeg is not installed. Installing..."
    sudo apt update
    sudo apt install -y ffmpeg
fi

# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies from requirements.txt (if it exists)
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Add any other setup tasks specific to your project below
# For example, you could run database migrations, set environment variables, etc.

# Deactivate the virtual environment
deactivate

echo "Project setup completed."