import requests
from bs4 import BeautifulSoup

def get_page(url):
    try:
        response = requests.get(url)
    except:
        return None

    return response


def find_links(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.find_all('td', limit=4)

if __name__ == "__main__":
    link = 'http://www.tsetmc.com/Loader.aspx?ParTree=15'
    response_page = get_page(link)
    links = find_links(response_page.text)
    print(links[2].contents[0],':',links[3].contents[0])


