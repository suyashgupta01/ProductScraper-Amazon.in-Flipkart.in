import bs4
import requests as rq
import itertools

to_search = input("Enter the product that you want to search on Amazon: ")
user_input = input("Enter the maximum price for the product: ")
max_price = int(user_input)

headers = {'User-Agent': 'Guptaji\'s_request'}
r = rq.get("https://www.amazon.in/s?k=" + to_search , headers = headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
products = soup.find_all('span', attrs = {'class' : 'a-size-medium a-color-base a-text-normal'}) # list of products
prices = soup.find_all('span', attrs = {'class' : 'a-price-whole'}) # list of prices

# there is A HUGE ISSUE in prices: ',' in b/w prices; so, can't convert to int
refined_prices = []
for item in prices:
    refined_prices.append(item.get_text().replace(',', ''))
# now filtering out prices under the amount given by user
req_list = [] # A list of lists: [product, price]
for (x,y) in zip(products, refined_prices):
    if int(y) <= max_price:
        item = [x.get_text(), y]
        req_list.append(item)

for item in req_list:
    print(item[0] + "\n" + item[1])