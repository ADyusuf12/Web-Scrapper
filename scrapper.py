import requests
from bs4 import BeautifulSoup
import pprint
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page_data(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        return BeautifulSoup(res.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None

def get_hn_data(pages):
    links, subtext = [], []
    for page in range(1, pages + 1):
        url = f'https://news.ycombinator.com/news?p={page}'
        soup = fetch_page_data(url)
        if soup:
            links.extend(soup.select('.titleline > a'))
            subtext.extend(soup.select('.subtext'))
    return links, subtext

def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(hn)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Scrape Hacker News for the top articles.')
    parser.add_argument('pages', type=int, help='Number of pages to scrape')
    args = parser.parse_args()

    logging.info(f"Scraping {args.pages} pages of Hacker News")
    links, subtext = get_hn_data(args.pages)
    top_articles = custom_hn(links, subtext)
    
    pprint.pprint(top_articles)

if __name__ == '__main__':
    main()
