import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parseArguments():
    parser = argparse.ArgumentParser(description="URL grabber script")
    parser.add_argument("url", type=str, help="The URL to start with")
    parser.add_argument("--recursive", action="store_true", help="Enable recursive URL grabbing")
    parser.add_argument("-o", "--output", type=str, help="Output file to write input fields")
    parser.add_argument("-u", "--user-agent", type=str, help="Custom user agent")
    return parser.parse_args()

def fetchHtml(url, user_agent=None):
    try:
        headers = {"User-Agent": user_agent} if user_agent else {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Can't fetch {url}: {e}")
        return None
    except KeyboardInterrupt:
        print("\n[-] CTRL + C: Exiting...")
        exit()

def extractUrls(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        full_url = urljoin(base_url, href)
        urls.append(full_url)
    return urls

def checkInputFields(html, url, output_file=None):
    soup = BeautifulSoup(html, 'html.parser')
    input_fields = soup.find_all('input')
    if input_fields:
        print(f"\nURL: {url}")
        for input_field in input_fields:
            print(input_field)
        print("-" * 50)
        if output_file:
            try:
                with open(output_file, 'a', encoding='utf-8') as f:
                    f.write(f"\nURL: {url}\n")
                    f.write("-" * 50 + "\n")
                    for input_field in input_fields:
                        f.write(str(input_field) + "\n")
            except Exception as e:
                print(f"Can't write {output_file}: {e}")

def main():
    args = parseArguments()
    print(f"URL: {args.url}")
    print(f"Recursive: {args.recursive}")
    if args.user_agent:
        print(f"User-Agent: {args.user_agent}")
    
    visited_urls = set()
    urls_to_visit = [args.url]
    
    print("-" * 50)
    while urls_to_visit:
        url = urls_to_visit.pop(0)
        visited_urls.add(url)
        
        htmlContent = fetchHtml(url, args.user_agent)
        if htmlContent:
            checkInputFields(htmlContent, url, args.output)
            
            if args.recursive:
                new_urls = extractUrls(htmlContent, url)
                for new_url in new_urls:
                    if new_url not in visited_urls and new_url not in urls_to_visit:
                        urls_to_visit.append(new_url)

if __name__ == "__main__":
    main()