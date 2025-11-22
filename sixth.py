import sys
import re
import requests


def download_url_and_get_all_hrefs(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Neplatny status code {response.status_code} pro URL {url}")
    html = response.text
    pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)
    hrefs = pattern.findall(html)
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        for href in hrefs:
            print(href)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
