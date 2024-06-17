import requests
from bs4 import BeautifulSoup

url = input('Enter the site URL: ')
try:
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Find all script tags and extract src attributes
        script_tags = soup.find_all('script')
        for script in script_tags:
            src = script.get('src')
            if src:
                print(src)
        
        # Find any inline JavaScript code within the HTML
        inline_scripts = soup.find_all('script', string=True)
        for script in inline_scripts:
            print(script.text.strip())

    else:
        print(f'Failed to retrieve content. Status code: {r.status_code}')

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')
