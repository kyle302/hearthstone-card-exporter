from bs4 import BeautifulSoup
import csv

# Prompt for the file location
file_location = input("Please enter the path to your file or drag and drop the file here: ").strip()

# Load and parse the HTML content from the text file
with open(file_location, 'r') as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

# Find the main card-list div
card_list = soup.find('div', id='card-list')

# Prepare data list for CSV
data = []

# Iterate through each card
for card in card_list.find_all('div', class_='collection-card'):
    card_name = card.find('img', alt=True)['alt']  # Get the card name from the alt attribute of img
    normal_count = card.find('div', class_='collection-counts').p.get_text(strip=True)
    golden_count = card.find('p', class_='count-golden').get_text(strip=True)
    
    data.append([card_name, normal_count, golden_count])

# Write data to CSV
with open('card_collection.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Card Name', 'Normal Count', 'Golden Count'])
    writer.writerows(data)

print("Data has been successfully written to card_collection.csv")
