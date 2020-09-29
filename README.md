# Consumer Electronics

Scrap the cigabuy website to get all consumer electronics form all pages and return csv file with title, url, discounted price and original price
- https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html

## Code style

- This project is written in python 3.
- Use Scrapy.

## Clone/Run app
````
# Clone repo
$ git clone https://github.com/MotazBellah/cigabuy

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ cd cigabuy
$  scrapy crawl consumer_electronics -o consumer_electronics.csv

````
