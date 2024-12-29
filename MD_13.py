from googlesearch import search
import time

query = 'inurl:ftp'
def perform_search(query):
    time.sleep(10)
    try:
        results = search(query, num_results=20)
        for url in results:
            print(url)
    
    except Exception as e:
        print(f"An error occurred: {e}")

perform_search(query)

# Output: An error occured: 429 Client Error: Too Many Requests for url:
# https://www.google.com/search?num=20&q=inurl%3Aftp+inurl%3Ahttp
