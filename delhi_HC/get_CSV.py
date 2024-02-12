# URL of the webpage containing the table
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
import csv
import sys

# Define download directory
download_dir = os.path.join(os.getcwd(), 'downloads')

# Set Chrome options to enable downloads
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": download_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Check if the year argument is provided
if len(sys.argv) < 2:
    print("Please provide the year as an argument.")
    sys.exit(1)

YEAR = int(sys.argv[1])
url = f"https://dhcbkp.nic.in/FreeText/{YEAR}.html"

# Navigate to the webpage with the file to download
driver.get(url)

table = driver.find_element(By.TAG_NAME, 'table')

# Find all rows within the table body
rows = table.find_elements(By.XPATH, "//tbody/tr")

with open(f'/home/anan/Desktop/legal_tech/data/table_data_{YEAR}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Iterate over each row in the table body
    for row in rows:
        # Extract the text from each cell in the row
        cells = row.find_elements(By.TAG_NAME, "td")
        data = [cell.text for cell in cells[:-1]]  # Exclude the last cell
        
        # Get the link from the last cell if available
        last_cell_link = cells[-1].find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        # Add the link to the data list
        data.append(last_cell_link)
        
        # Write the row of data to the CSV file
        writer.writerow(data)

# Close the browser
driver.quit()
