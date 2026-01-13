# Development Container Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## What's Configured

- **Base Image**: Python 3.11
- **Extensions**:
  - Python language support
  - Jupyter notebook support
  - Enhanced code completion with Pylance
- **Dependencies**: Automatically installs from `Requirements.txt`
- **Port Forwarding**: Port 8888 for Jupyter notebooks
- **Output Directory**: Automatically created on container start

## Usage

### GitHub Codespaces

1. Click the "Code" button on GitHub
2. Select "Create codespace on [branch]"
3. Wait for the container to build and dependencies to install
4. Start coding!

### VS Code Dev Containers

1. Install the "Dev Containers" extension
2. Open this repository in VS Code
3. Press F1 and select "Dev Containers: Reopen in Container"
4. Wait for the container to build

## Running the Demo

Once the container is ready:

```bash
# Run the static animation
python src/main.py

# Start Jupyter for interactive demo
jupyter notebook notebooks/interactive_demo.ipynb
```

The output will be saved to the `output/` directory.
