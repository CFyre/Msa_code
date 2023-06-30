import requests
from bs4 import BeautifulSoup

def main():
    symbol = 'AAPL'
    url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
    headers = {"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    

    #request page
    response = requests.get(url, headers=headers)

    #parse html using beautiful soup
    soup = BeautifulSoup(response.text, 'html.parser')

    stock_dictionary = {}
    counter = 1
    for cell in soup.find_all('td'):
        if counter % 2 != 0:
            key = cell.text
        else:
            value = cell.text
            stock_dictionary[key] = value
        counter += 1
    print(stock_dictionary)
    
main()