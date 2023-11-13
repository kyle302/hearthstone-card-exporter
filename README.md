# hearthstone-card-exporter
A python script to create a .CSV of collected cards based on hsreplay.net collection
Collects card name, card counts from hsreplay <div> fields

Requirements:
Python, BS4,Collection uploaded to hsreplay.net

Instructions:
1. Upload your collection to hsreplay.net using Hearthstone Deck Tracker
2. Install BS4 - in your terminal window enter "pip3 install bs4"
3. Browse to https://hsreplay.net/collection/mine/ and scroll ALL THE WAY DOWN so all of your collection/cards are rendered on the page
4. Right click the page - click inspect
5. Click on "main class="card-list-wrapper" to expand the selection
6. Right click "div id="card-list" - Copy - Copy Element
7. Paste the element into your text editor and save the file, example collection.txt
8. Download and run the repo's python script, run it - 
python3 hscollection.py 
9. Drag & drop your collection.txt into the python window when prompted, hit enter
10. Your collection will be sorted into a .csv showing card name, card counts and golden card counts
