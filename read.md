# JavaScript Extractor

This Python script extracts JavaScript URLs and inline scripts from a specified website URL.

## Overview

This script uses the `requests` library to fetch the webpage content and `BeautifulSoup` for parsing HTML. It identifies and extracts both external JavaScript URLs (`<script src="...">`) and inline JavaScript code blocks (`<script>...</script>`).

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)

## Usage

1. **Clone the repository**
2. Install dependencies:
```
pip install requests beautifulsoup4
```
3. Run the script:
```
python javascript_extractor.py
```
