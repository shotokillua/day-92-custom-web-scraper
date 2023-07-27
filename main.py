from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

chromedriver_autoinstaller.install()

chrome_driver_path = "D:\Development\chromedriver.exe"

# Set up Chrome Options
options = webdriver.ChromeOptions() # this allows you to set options such as enabling headless mode or customize other behaviors of the Chrome browser
options.add_experimental_option("detach", True) # this will keep the browser window open after the webdriver is closed - good for troubleshooting

# Initialize the Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service) # or driver = webdriver.Chrome(service=service, options=options)

# Access the link
driver.get("https://www.nba.com/stats/players/traditional")
driver.maximize_window()
driver.implicitly_wait(5)

# Find the table element by its XPath, CSS selector, or other locators
table_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')

# Initialize lists to store the table data
rows = []
header_row = []

# Extract the header row (if applicable)
header_row_elements = table_element.find_elements(By.TAG_NAME, 'th')
header_row = [header.text.strip() for header in header_row_elements]

# Extract the data rows
data_rows_elements = table_element.find_elements(By.TAG_NAME, 'tr')
for row in data_rows_elements:
    cell_elements = row.find_elements(By.TAG_NAME, 'td')
    row_data = [cell.text.strip() for cell in cell_elements]
    rows.append(row_data)

# Now you have the header_row and rows containing the table data
# print(header_row)
# print(rows)

list_of_dict = []

for row in rows[1:]:

    row_dict = {
        header_row[1]: row[1],
        header_row[2]: row[2],
        header_row[3]: row[3],
        header_row[4]: row[4],
        header_row[5]: row[5],
        header_row[6]: row[6],
        header_row[7]: row[7],
        header_row[8]: row[8],
        header_row[9]: row[9],
        header_row[10]: row[10],
        header_row[11]: row[11],
        header_row[12]: row[12],
        header_row[13]: row[13],
        header_row[14]: row[14],
        header_row[15]: row[15],
        header_row[16]: row[16],
        header_row[17]: row[17],
        header_row[18]: row[18],
        header_row[19]: row[19],
        header_row[20]: row[20],
        header_row[21]: row[21],
        header_row[22]: row[22],
        header_row[23]: row[23],
        header_row[24]: row[24],
        header_row[25]: row[25],
        header_row[26]: row[26],
        header_row[27]: row[27],
        header_row[28]: row[28],
        header_row[29]: row[29],
    }

    list_of_dict.append(row_dict)

print(list_of_dict)

# Specify the file name for the CSV file
csv_file_name = "output.csv"

# List of field names (header_row in your case)
field_names = ["PLAYER", "TEAM", "AGE", "GP", "W", "L", "MIN", "PTS", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%", "OREB", "DREB", "REB", "AST", "TOV", "STL", "BLK", "PF", "FP", "DD2", "TD3", "+/-"]

# Write the list of dictionaries into the CSV file
with open(csv_file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=field_names)

    # Write the header row
    writer.writeheader()

    # Write each dictionary as a row in the CSV file
    writer.writerows(list_of_dict)

print(f"CSV file '{csv_file_name}' created successfully.")

# Read the CSV file and store the data in a list of dictionaries
data = []
with open(csv_file_name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Take user inputs for player name and statistic category
player_name = input("Enter the player name: ")
statistic_category = input("Enter the statistic category: ")

# Search for the player's row in the data list based on the player name
player_row = None
for row in data:
    if row["PLAYER"] == player_name:
        player_row = row
        break

# If the player name is not found in the CSV file, print an error message and exit
if player_row is None:
    print(f"Player '{player_name}' not found in the CSV file.")
    exit()

# Retrieve the value for the specified statistic category from the player's row
# Assuming the statistic category column has numeric values in the CSV file
statistic_value = float(player_row.get(statistic_category, 0))

# Print the result
print(f"The value of '{statistic_category}' for '{player_name}' is: {statistic_value}")