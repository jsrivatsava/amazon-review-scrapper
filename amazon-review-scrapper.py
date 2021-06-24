import sys, os, os.path
from os import path
from amazon_product_review_scraper import amazon_product_review_scraper
folder_path = None
# Create result folder
if len(sys.argv) > 1 and not path.exists('reviews'):
    folder_path = os.path.join(os.getcwd(), 'reviews')
    os.mkdir(folder_path)
    
# Process asins
for i, args in enumerate(sys.argv):
    if i > 0:
        review_scraper = amazon_product_review_scraper(amazon_site="amazon.in", product_asin=args)
        reviews_df = review_scraper.scrape()
        print(os.getcwd() + "/reviews/" + args + ".csv")
        reviews_df['content'].to_csv(os.getcwd() + "/reviews/" + args + ".csv")