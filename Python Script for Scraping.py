import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_reviews(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    
    for item in soup.find_all('div', class_='product'):  # Modify selector based on the site
        name = item.find('span', class_='product-name').text.strip()
        price = item.find('span', class_='product-price').text.strip()
        rating = item.find('span', class_='average-rating').text.strip()
        review_count = item.find('span', class_='review-count').text.strip()

        reviews = item.find_all('span', class_='review-text')
        review_texts = [review.text.strip() for review in reviews[:3]]  # Limit to 3 recent reviews

        products.append([name, price, rating, review_count, review_texts])

    return products

# Scrape the data
url = "https://www.example.com/category-page"
data = scrape_product_reviews(url)

# Save the data to a CSV file.
with open("ecommerce_product_reviews.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Product Price", "Average Rating", "Number of Reviews", "Review Text"])
    writer.writerows(data)

print("Scraping completed and data saved to ecommerce_product_reviews.csv")
