import crawler
import csv

fetcher = crawler.ArticleFetcher()

with open('crawler_output.csv', 'w', newline='') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for article in fetcher.fetch():
        articlewriter.writerow([article.emoji, article.title, article.image, article.content])   