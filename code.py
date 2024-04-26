# Attempting to extract the specified part of the table and convert it to a pandas dataframe
# Re-loading the HTML file to parse the content with BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML content
file_path = 'C:/Users/dhana/OneDrive/Desktop/tally/results/netprofit.html'
with open(file_path, 'r') as file:
    content = file.read()

 

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

 

# Find all the table rows in the HTML content
rows = soup.find_all('tr')

 

# Initialize an empty list to store the extracted data
extracted_data = []

 

# Iterate through each row and extract columns of interest (Particulars and Debit)
for row in rows:
    # Extract all the columns (td) in the row
    cols = row.find_all('td')

    # Check if the row contains data of interest based on expected number of columns
    if len(cols) > 10:
        particulars=cols[2].get_text(strip=True)
        amount=cols[9].get_text(strip=True)
        # if particulars and not particulars.isspace() and amount and not amount.isspace():
        extracted_data.append([particulars,amount])
        

 

# # # # # Create a pandas DataFrame from the extracted data
particulars_debit_df = pd.DataFrame(extracted_data, columns=['Particulars','amount'])
# # particulars_debit_df.to_csv('salesaccount.csv')
print(particulars_debit_df)
