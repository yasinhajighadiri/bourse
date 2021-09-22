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
    return soup.text

if __name__ == "__main__":
    link = 'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=6110133418282108&c=44%20'
    response_page = get_page(link)
    links = find_links(response_page.text)
    stock_market_share=links.split(',')
    print('قیمت پایانی :',stock_market_share[3])

