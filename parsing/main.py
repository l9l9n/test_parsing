import requests
from bs4 import BeautifulSoup

url = 'https://www.kivano.kg/noutbuki'

headers = {
    "Accept": "*/*",
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text
# print(src)
with open('index.html', 'w', encoding='utf8') as file:
    file.write(src)

# soup = BeautifulSoup(req.text, 'lxml')
#
# # all_item_products = soup.find(class_='list-view').find(class_="item product_listbox oh").find(class_="product_text pull-left")
# prod = soup.find_all('div', class_="listbox_title oh")
# # item = all_item_products.get('listbox_title oh')
# print(prod)
#
# # for item in prod:
# #     item_text = item.text
# #     print(item_text)

