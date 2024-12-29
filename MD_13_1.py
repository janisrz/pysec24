import time
import random
from googlesearch import search

def perform_search_with_sleep(query, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            # Perform the search and retrieve results
            results = search(query, num_results=20)  # No pause parameter here
            
            # Print each result
            for url in results:
                print(url)
                time.sleep(2)  # Introduce a 2-second delay between printing URLs

            return  # Exit if successful

        except Exception as e:
            if '429' in str(e):  # Check if the error is a 429 error
                retries += 1
                wait_time = (2 ** retries) + random.uniform(0, 1)  # Exponential backoff with jitter
                print(f"429 Too Many Requests: Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)  # Wait before retrying
            else:
                print(f"An error occurred: {e}")
                break  # Exit on other errors

# Define your query
query = 'inurl:ftp inurl:http'

# Execute the function
perform_search_with_sleep(query)
