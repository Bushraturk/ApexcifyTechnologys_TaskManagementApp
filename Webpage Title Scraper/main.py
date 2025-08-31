import requests
import re


def scrape_title(url: str):
    """Fetches a webpage and extracts its <title>"""

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
            if match:
                title = match.group(1).strip()
                with open("title.txt", "w", encoding="utf-8" ) as f:
                    f.write(title)
                    print(f"Title saved to title.txt: {title}")

            else:
                print("No title tag found.")

        else: 
            print(f"Failed to fetch webpage. status code: {response.status_code}")    
    
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None



   


if __name__ == "__main__":
    url = "https://hackthon3-tawny.vercel.app"
    scrape_title(url)
