import sys
import requests
from bs4 import BeautifulSoup
import time


def is_valid_link(link):
    href = link['href']
    if (href.startswith('#') or 'Help:' in href or 'File:' in href):
        return False

    if link.find_parent(['i', 'em', 'table', 'sup']):
        return False

    if not href.startswith('/wiki/'):
        return False

    return True


def get_first_link(url, history):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        content_div = soup.find('div', id='mw-content-text')

        if not content_div:
            return None

        for element in content_div.find_all('p'):
            if element.name == 'p' and not element.text.strip():
                continue

            for link in element.find_all('a', href=True):
                if is_valid_link(link):
                    href = link['href']
                    full_url = "https://en.wikipedia.org" + href
                    if full_url not in history:
                        return full_url

        print("It leads to a dead end!")
        return None

    except requests.exceptions.RequestException as e:
        if e.response.status_code == 404:
            print("It leads to a dead end!")
        else:
            print(f"{type(e).__name__}: {e}")
        return None

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py <url>")
        sys.exit(1)

    article_name = sys.argv[1].replace(' ', '_')
    base_url = 'https://en.wikipedia.org/wiki/'
    visited_urls = []
    current_url = base_url + article_name

    while True:
        if current_url in visited_urls:
            print("It leads to an infinite loop!")
            break

        visited_urls.append(current_url)

        if current_url.endswith('Philosophy'):
            print(f"{len(visited_urls)} roads from {visited_urls[0].split('/')[-1].replace('_', ' ')} to Philosophy!")
            break

        next_url = get_first_link(current_url, visited_urls)
        if not next_url:
            break

        print(current_url.split('/')[-1].replace('_', ' '))

        current_url = next_url
        time.sleep(0.5)


if __name__ == "__main__":
    main()
