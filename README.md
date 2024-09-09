# ClipCoords
[![DOI](https://zenodo.org/badge/854333898.svg)](https://zenodo.org/doi/10.5281/zenodo.13733593)
![GitHub Release](https://img.shields.io/github/v/release/hfkroes/ClipCoords?color=green)
![GitHub top language](https://img.shields.io/github/languages/top/hfkroes/ClipCoords?color=yellow)
![GitHub License](https://img.shields.io/github/license/hfkroes/ClipCoords?color=orange)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/hfkroes/ClipCoords?color=red)

**ClipCoords** is a Python script that allows you to easily transfer coordinate values from Google Maps to Excel datasheets. It monitors your clipboard for floating-point coordinates in the Google Maps compatible format, automatically formats the values into tab-separated format, and updates your clipboard. This allows you to paste the numbers directly into two adjacent cells in Excel by simply pressing `Ctrl+V` in a single interaction.

## Features

- Monitors clipboard for coordinate-like values.
- Converts periods to commas in floating-point numbers.
- Formats the numbers for pasting into two separate Excel cells in a single interaction.
- Supports both positive and negative numbers.
- Provides live debug information from clipboard in cmd.

## Installation

### Requirements

- Python 3.x
- `pyperclip` (for clipboard interaction)
- `pynput` (for detecting clipboard changes)

### Step-by-Step Installation

1. Clone this repository:
```bash
  git clone https://github.com/your-username/clipcoords.git
   ```
   
2. Navigate to the project directory:

  ```bash
  cd clipcoords
  ```

3. Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```
4. Run the script:

  ```bash
  python clipcoords.py
  ```
## Usage
1. Run the script: Start the program with python clipcoords.py. It will run in the background, continuously monitoring your clipboard.

2. Copy coordinates: Copy any coordinates from Google Maps by right clicking an adress and left clicking its coordinate values.

3. Paste in Excel: Go to Excel, select a cell, and press Ctrl+V. The numbers will be pasted into two adjacent cells automatically.

## Citation
If you use ClipCoords in your work or project, please cite it as follows:

```txt
Author: Hector Kroes
Project: ClipCoords
URL: https://github.com/your-username/clipcoords
DOI: 10.5281/zenodo.13733594
Year: 2024
```
