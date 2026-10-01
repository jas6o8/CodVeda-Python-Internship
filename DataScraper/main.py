from bs4 import BeautifulSoup
import requests
import csv
import os

# 1. Fetch and parse the website
source = requests.get('https://quotes.toscrape.com').text
soup = BeautifulSoup(source, 'lxml')

# 2. Find ALL quotes on the page (not just the first one)
quotes = soup.find_all('div', class_='quote')

# 3. Define the CSV file name and get the correct directory path
csv_file_name = 'quotes_data.csv'
# This gets the folder where your main.py script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, csv_file_name)

# 4. Open the CSV file and write the data
# 'w' means write mode, newline='' prevents extra blank lines in the CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Author', 'Quote', 'Tags'])
    
    # Loop through every quote found on the page
    for quote in quotes:
        # Extract the data for this specific quote
        author = quote.find('small', class_='author').text
        message = quote.span.text
        
        # Get all tags and join them into a single string separated by commas
        tags_list = [tag.text for tag in quote.find_all('a', class_='tag')]
        tags_string = ", ".join(tags_list)
        
        # Write this quote's data as a new row in the CSV
        writer.writerow([author, message, tags_string])

print(f"Successfully saved data to {file_path}")