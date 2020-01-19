import requests as rq
import bs4

to_search = input("Enter the product that you want to search on Flipkart: ")
user_input = input("Enter the maximum price for the product: ")
max_price = int(user_input)

headers = {'User-Agent': 'Guptaji\'s_request'}
r = rq.get("https://www.flipkart.com/search?q=" + to_search, headers=headers)
soup = bs4.BeautifulSoup(r.text, 'html.parser')
products = soup.findAll('div', attrs={'class': '_3wU53n'})  # list of products
prices = soup.findAll('div', attrs={'class': '_1vC4OE _2rQ-NK'})  # list of prices

# there are 2 ISSUES in prices:
# 1) ',' in b/w prices; so, can't convert to int
# 2) rupee symbol at the beginning of each price
refined_prices = []
for item in prices:
    refined_item = item.get_text().replace(',', '')
    refined_item = refined_item.replace('₹', '')
    refined_prices.append(refined_item)

# now filtering out prices under the amount given by user
req_list = []  # A list of lists: [product, price]
for (x, y) in zip(products, refined_prices):
    if int(y) <= max_price:
        item = [x.get_text(), y]
        req_list.append(item)

for item in req_list:
    print(item[0] + "\n" + item[1])