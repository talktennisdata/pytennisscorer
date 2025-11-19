# PyTennisScorer Interactive Documentation

This is the Quarto Live documentation for PyTennisScorer, which allows users to run Python code directly in their browser using Pyodide.

## Features

- Interactive Python code execution in the browser
- No installation required for users
- Loads `pytennisscorer` directly from PyPI
- Live code examples that users can modify and run

## Local Development

### Prerequisites

1. Install Quarto from https://quarto.org/docs/get-started/
2. Install the Quarto Live extension (will be done automatically on first render)

### Building Locally

```bash
cd docs-quarto
quarto add r-wasm/quarto-live --no-prompt  # Install extension (first time only)
quarto render
```

The documentation will be built in the `_site` directory.

### Preview Locally

```bash
cd docs-quarto
quarto preview
```

This will open the documentation in your browser with live reload.

## How It Works

1. **Pyodide Integration**: The documentation uses Pyodide to run Python code in the browser
2. **PyPI Package Loading**: `pytennisscorer` is automatically installed from PyPI when the page loads
3. **Live Code Blocks**: Code blocks with `#| live: true` become interactive

## Deployment

The documentation is automatically built and deployed to GitHub Pages when changes are pushed to the master branch.

The GitHub Actions workflow:
1. Sets up Python and Quarto
2. Installs the Quarto Live extension
3. Renders the documentation
4. Deploys to GitHub Pages

## File Structure

- `index.qmd` - Main documentation page with interactive examples
- `_quarto.yml` - Quarto configuration
- `setup-pyodide.js` - Custom Pyodide setup to load pytennisscorer from PyPI
- `*.scss` - Custom styling