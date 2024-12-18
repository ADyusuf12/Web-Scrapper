# Web Scraper

## Introduction
**Web Scraper** is a Python script designed to scrape top articles from Hacker News. It uses the BeautifulSoup and requests libraries to parse HTML content and extract useful information. This script allows users to specify the number of pages to scrape, handles errors gracefully, and uses logging for better traceability.

## Features
- **Scrape Multiple Pages:** Specify the number of pages to scrape from Hacker News.
- **Error Handling:** Gracefully handles errors and logs them.
- **Command-Line Arguments:** Use argparse to specify the number of pages to scrape.
- **BeautifulSoup Integration:** Parse and extract HTML content easily.
- **Logging:** Detailed logging of the scraping process.

## Technologies Used
- **Python**
- **BeautifulSoup:** Library for parsing HTML and XML documents.
- **requests:** Library for making HTTP requests.

## Installation Instructions
1. **Clone the repository:**
   git https://github.com/ADyusuf12/Web-Scrapper.git
   cd web-scraper
2. **Create a virtual environment and activate it (optional but recommended)**

## Usage
**Run the script with the number of pages to scrape as an argument:**

python scraper.py <number_of_pages>

Example:

python scraper.py 2

**View the output:**
 The script will print the top articles to the console.

 ## Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature-branch).

Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Thanks to the BeautifulSoup and requests developers for their excellent libraries.

Inspired by various open-source web scraping tools.
