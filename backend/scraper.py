import requests
from bs4 import BeautifulSoup
import redis
import json


def scrape_page_elements(url):
    """
    Scrape head, header, and products from Croma website.
    Returns all scraped data as a dictionary.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    head = soup.head
    header = soup.find('div', class_='bs-header')

    products = []
    product_list = soup.find('ul', class_='product-list')
    if product_list:
        for item in product_list.find_all('li', class_='product-item', recursive=False):
            product = {}

            title_tag = item.find('h3', class_='product-title')
            if title_tag and title_tag.a:
                product['title'] = title_tag.a.get_text(strip=True)
                product['link'] = 'https://www.croma.com' + title_tag.a['href']
            else:
                product['title'] = None
                product['link'] = None

            new_price_tag = item.find('span', {'data-testid': 'new-price'})
            product['price'] = new_price_tag.get_text(strip=True) if new_price_tag else None

            old_price_tag = item.find('span', {'data-testid': 'old-price'})
            product['old_price'] = old_price_tag.get_text(strip=True) if old_price_tag else None

            discount_tag = item.find('span', class_='discount')
            product['discount'] = discount_tag.get_text(strip=True) if discount_tag else None

            tags = [tag.get_text(strip=True) for tag in item.find_all('span', class_='tagsForPlp')]
            product['tags'] = tags

            product['product_id'] = item.find('div', class_='cp-product')['id'] if item.find('div', class_='cp-product') else None

            products.append(product)

    response = {
        "head": str(head) if head else None,
        "header": str(header) if header else None,
        "products": products,
    }
    # print(response)
    print("Scraping completed")
    return response


def store_in_redis(data):
    """
    Save scraped data to Redis database, under the key 'scraped_content'.
    """
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set("scraped_content", json.dumps(data))
    print("Data stored in redis")


if __name__ == "__main__":
    url = "https://www.croma.com/televisions-accessories/c/997"
    page_elements = scrape_page_elements(url)
    store_in_redis(page_elements)