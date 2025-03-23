# ebay-tech-deals
scrapes e-bay global tech deals  every 3 hours for 2 days.

# eBay Tech Deals Scraper 
COSC 482 – Data Science and Web Scraping 

 **Overview

This project was built as part of a lab assignment to practice building a full data pipeline using Python, GitHub Actions, and exploratory data analysis.

The goal was to scrape live product data from eBay's Global Tech Deals page, collect it over time using automation, clean and process the data, and explore it using visualizations.

---

##  What This Project Does

###  1. Scraping with Selenium  
The `scraper.py` script uses Selenium to load the entire Tech Deals page (including lazy-loaded items), extract product details like title, price, original price, shipping info, and the product URL, then appends it to a CSV file with a timestamp.

###  2. Automation with GitHub Actions  
A GitHub Actions workflow (`scrape.yml`) runs the scraper every 2 hours, allowing the dataset to grow automatically over time — hands-free!

### 3. Cleaning with Pandas  
The `clean_data.py` script processes the raw CSV:
- Cleans and converts price columns
- Fills missing values
- Adds a `discount_percentage` column

### 4. EDA with Jupyter Notebook  
The `EDA.ipynb` notebook walks through:
- Time series analysis of scraping frequency
- Price and discount distributions
- Shipping info breakdown
- Text analysis of product titles
- Price difference calculations
- Top 5 highest discounts

---

##  Key Insights

- Discounts vary widely, with some products going over 70% off.
- Most commonly featured brands: **Apple**, **Samsung**, and **iPhone**.
- Shipping information is inconsistent, with many items not displaying it clearly.
- Deal updates appear more frequently during certain hours.

---

