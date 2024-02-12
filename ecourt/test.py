from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By

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

# Navigate to the webpage with the file to download
driver.get("https://judgments.ecourts.gov.in/pdfsearch/index.php")



# Wait for the download to complete
time.sleep(15)  # Adjust this time according to the size of the file and internet speed



row_index = 1  # Replace with the index of the row where the button is located
column_index = 2  # Replace with the index of the column where the button is located
row_xpath = f"//table[@id='example_pdf']/tbody/tr[{row_index}]"
column_xpath = f"{row_xpath}/td[{column_index}]"


button = driver.find_element(By.XPATH, f"{column_xpath}//button[@id='link_0']")
button.click()

time.sleep(5)

row_index = 5  # Replace with the index of the row where the button is located
column_index = 2  # Replace with the index of the column where the button is located
row_xpath = f"//table[@id='example_pdf']/tbody/tr[{row_index}]"
column_xpath = f"{row_xpath}/td[{column_index}]"



time.sleep(5)

button = driver.find_element(By.XPATH, f"{column_xpath}//button[@id='link_0']")
button.click()




driver.quit()