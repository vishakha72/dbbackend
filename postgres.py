import pandas as pd
from sqlalchemy import create_engine

# Set up the PostgreSQL connection
engine = create_engine('postgresql://postgres.lonxcalhvgrfsgplpoqv:FinkeepRaghav@aws-0-ap-south-1.pooler.supabase.com:6543/postgres')
# Example: Create a Pandas DataFrame
# data = {
#     'column1': [2, 1, 3],
#     'column2': ['A', 'B', 'C']
# }
# df = pd.DataFrame(data)

# # Store the DataFrame in the PostgreSQL server
# df.to_sql('firsttable', con=engine, if_exists='replace', index=False)
csv_file_path ="C:/Users/hp/whole.csv"
df = pd.read_csv(csv_file_path)
# Replace 'your_table_name' with the desired table name
table_name = 'Whole'

# Store the DataFrame in the specified table in the PostgreSQL server
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

import json
import pandas as pd
from bs4 import BeautifulSoup
import aiofiles
import asyncio
import asyncpg

async def Dataframe1(file_path):
    # Read the HTML content
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

        # Check if the row contains data of interest based on the expected number of columns
        if len(cols) > 29:
            particulars = cols[1].get_text(strip=True)
            value = cols[29].get_text(strip=True)

            # Add the extracted data to the list if it's not empty or a space character
            if particulars and not particulars.isspace() and value and not value.isspace():
                extracted_data.append([particulars, value])

    # Create a pandas DataFrame from the extracted data
    dataframe = pd.DataFrame(extracted_data, columns=['Particulars', 'Value'])
    return dataframe

async def Dataframe2(file_path1):
    # Read the HTML content asynchronously
    async with aiofiles.open(file_path1, 'r') as file:
        content = await file.read()

    # Create a DataFrame from the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('tr')

    # Extract data into a list
    extracted_data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 29:
            particulars = cols[1].get_text(strip=True)
            value = cols[29].get_text(strip=True)
            if particulars and not particulars.isspace() and value and not value.isspace():
                extracted_data.append([particulars, value])
    dataframe1 = pd.DataFrame(extracted_data, columns=['Particulars', 'Value'])

    return dataframe1

async def Dataframe3(file_path2):
    # Read the HTML content asynchronously
    async with aiofiles.open(file_path2, 'r') as file:
        content = await file.read()

    # Create a DataFrame from the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('tr')

    # Extract data into a list
    extracted_data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 29:
            particulars = cols[1].get_text(strip=True)
            value = cols[29].get_text(strip=True)
            if particulars and not particulars.isspace() and value and not value.isspace():
                extracted_data.append([particulars, value])
    dataframe2 = pd.DataFrame(extracted_data, columns=['Particulars', 'Value'])

    return dataframe2

async def Card1(dataframe):
    df1 = pd.DataFrame(dataframe['Value'])
    df1['Value'] = pd.to_numeric(df1['Value'].str.replace(',', ''), errors='coerce')
    df1['Value'].fillna(0, inplace=True)
    df1['Value'] = df1['Value'].astype(float)
    maxi = df1.sort_values(by='Value', ascending=False)
    return maxi.head(10).to_dict(orient='records')

async def Card2(dataframe1):
    df1 = pd.DataFrame(dataframe1['Value'])
    df1['Value'] = pd.to_numeric(df1['Value'].str.replace(',', ''), errors='coerce')
    df1['Value'].fillna(0, inplace=True)
    df1['Value'] = df1['Value'].astype(float)
    maxi = df1.sort_values(by='Value', ascending=False)
    return maxi.head(10).to_dict(orient='records')

async def Card3(df):
    df1 = pd.DataFrame(df['Value'])
    df1['Value'] = pd.to_numeric(df1['Value'].str.replace(',', ''), errors='coerce')
    df1['Value'].fillna(0, inplace=True)
    df1['Value'] = df1['Value'].astype(float)
    maxi = df1.sort_values(by='Value', ascending=False)
    return maxi.head(10).to_dict(orient='records')

async def fetch_and_display():
    # Replace the file paths with your actual file paths
    file_path = 'C:/Users/hp/OneDrive/Desktop/Extraction-From-Tally--main/Results/stocksummary6.html'
    file_path1 = 'C:/Users/hp/OneDrive/Desktop/Extraction-From-Tally--main/Results/stocksummary3.html'
    file_path2 = 'C:/Users/hp/OneDrive/Desktop/Extraction-From-Tally--main/Results/stocksummary.html'

    dataframe = await Dataframe1(file_path)
    dataframe1 = await Dataframe2(file_path1)
    dataframe2 = await Dataframe3(file_path2)

    json1 = await Card1(dataframe)
    json2 = await Card2(dataframe1)
    json3 = await Card3(dataframe2)

    result_list = [
        {"Category": "StockName", "Card1": json1},
        {"Category": "StockName", "Card2": json2},
        {"Category": "StockName", "Card3": json3}
    ]

    return json.dumps(result_list, indent=2)




# Example usage:
if __name__ == "__main__":
    print(asyncio.run(fetch_and_display()))




async def fetch_and_display():
    DATABASE_URL = 'postgresql://postgres.lonxcalhvgrfsgplpoqv:FinkeepRaghav@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'
    pool = await asyncpg.create_pool(DATABASE_URL, statement_cache_size=0)
    
    try:
        async with pool.acquire() as connection1:
            columns_to_fetch = ["Value", 'SUM(CAST(REPLACE("Value", \',\', \'\') AS numeric)) AS total_value','COUNT(*) AS count']
            table_name = '"Whole"'
            query = f"SELECT {', '.join(columns_to_fetch)} FROM {table_name} GROUP BY Value ORDER BY Value DESC LIMIT 10;"
            records = await connection1.fetch(query)
            
            dataframe = pd.DataFrame(records, columns=["Particulars", "Values"])
            Whole = dataframe.iloc[0]['Values']
            October = dataframe.iloc[0]['Values']
            Decmeber = dataframe.iloc[9]['Values']
            # total_footfall2 = dataframe.iloc[9]['count']
            
            result_list = [
                {"Label": "Whole", "Value": Whole, "IconName": "MdDashboard"},
                {"Label": "October", "Value": October, "IconName": "MdDashboard"},
                {"Label": "December", "Value": Decmeber, "IconName": "MdDashboard"},
                # {"Label": "total footfall2", "Value": total_footfall2, "IconName": "MdDashboard"}
            ]
    finally:
        await pool.close()

    return result_list

# Run the asyncio event loop
print(asyncio.run(fetch_and_display()))
ᐧ
Page 2 of 14
extraction. Press tab to insert.
