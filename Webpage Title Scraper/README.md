# Webpage Title Scraper

A simple Python project to fetch and extract the `<title>` of any webpage and save it to a file (`title.txt`).

## Features
- Fetches a webpage using its URL
- Extracts the content of the `<title>` HTML tag
- Saves the title to a file (`title.txt`)
- Handles errors and missing title tags gracefully

## Requirements
- Python 3.11+
- [requests](https://pypi.org/project/requests/)

## Installation
1. Clone or download this repository.
2. (Optional) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
   Or, if using `pyproject.toml`:
   ```powershell
   pip install requests
   ```

## Usage
1. Open `main.py` and set the `url` variable to the webpage you want to scrape:
   ```python
   url = "https://hackthon3-tawny.vercel.app"
   scrape_title(url)
   ```
2. Run the script:
   ```powershell
   python main.py
   ```
3. The title will be saved in `title.txt` and printed in the terminal.

## Example Output
- If the webpage title is `Shopping Website`, then `title.txt` will contain:
  ```
  Shopping Website
  ```

## Project Structure
```
main.py           # Main script to run the scraper
pyproject.toml    # Project metadata and dependencies
README.md         # Project documentation
title.txt         # Output file for the scraped title
uv.lock           # Dependency lock file
```

## License
This project is for educational purposes.
