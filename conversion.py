# import pandas as pd

# # Read the text file with delimiter
# with open('C:/Users/hp/OneDrive/Desktop/finkeep/AAKPM3407D-2023.txt', 'r') as file:
#     lines = file.readlines()

# # Initialize an empty list to store rows
# data = []

# # Process each line in the file
# for line in lines:
#     # Split the line by '^' delimiter
#     values = line.strip().split('^')
#     # Append the split values to the data list
#     data.append(values)

# # Create a DataFrame from the data
# df = pd.DataFrame(data)

# # Step 2: Split column by delimiter
# df = pd.DataFrame(df.values.tolist(), columns=df.columns)

# # Step 3: Change first column from text to number
# df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

# # Step 4: Replace errors into null
# df = df.replace({'ERROR': pd.NA})

# # Step 5: Fill down the value for specific column (e.g., 'column_name')
# df.iloc[:, 0].fillna(method='ffill', inplace=True)

# # Step 6: Filter the rows based on a condition (e.g., filter rows where a specific column value is not null)
# df = df[df.iloc[:, 1].notnull()]
# df= df.iloc[5:75]
# df.drop(df.columns[6], axis=1, inplace=True)

# # Write the modified DataFrame to an Excel file
# df.to_excel('output_file2.xlsx', index=False, header=False)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# import pandas as pd

# # Read the text file with delimiter
# with open('C:/Users/hp/OneDrive/Desktop/finkeep/AAKPM3407D-2023.txt', 'r') as file:
#     lines = file.readlines()

# # Initialize an empty list to store rows
# data = []

# # Process each line in the file
# for line in lines:
#     # Split the line by '^' delimiter
#     values = line.strip().split('^')
#     # Append the split values to the data list
#     data.append(values)

# # Create a DataFrame from the data
# df = pd.DataFrame(data)

# # Step 2: Split column by delimiter
# df = pd.DataFrame(df.values.tolist(), columns=df.columns)

# # Step 3: Change first column from text to number
# df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

# # Step 4: Replace errors into null
# df = df.replace({'ERROR': pd.NA})

# # Step 5: Fill down the value for specific column (e.g., 'column_name')
# df.iloc[:, 0].fillna(method='ffill', inplace=True)

# # Step 6: Fill down the value in the second column until a different name appears
# current_index = df.iloc[0, 0]
# current_name = df.iloc[0, 1]
# for i in range(1, len(df)):
#     if pd.isna(df.iloc[i, 1]):
#         df.iloc[i, 1] = current_name
#     elif df.iloc[i, 0] != current_index:
#         current_index = df.iloc[i, 0]
#         current_name = df.iloc[i, 1]
#     else:
#         continue

# # Step 7: Filter the rows based on a condition (e.g., filter rows where a specific column value is not null)
# df = df[df.iloc[:, 1].notnull()]
# df = df.iloc[5:75]
# df.drop(df.columns[6], axis=1, inplace=True)

# # Write the modified DataFrame to an Excel file
# df.to_excel('output_file.xlsx', index=False, header=False)

# -------------------------------------------------------------------------------------------------------------------------------------------------



# import pandas as pd

# # Read the text file with delimiter
# with open('C:/Users/hp/OneDrive/Desktop/finkeep/AAKPM3407D-2023.txt', 'r') as file:
#     lines = file.readlines()

# # Initialize an empty list to store rows
# data = []

# # Process each line in the file
# for line in lines:
#     # Split the line by '^' delimiter
#     values = line.strip().split('^')
#     # Append the split values to the data list
#     data.append(values)

# # Create a DataFrame from the data
# df = pd.DataFrame(data)

# # Step 2: Split column by delimiter
# df = pd.DataFrame(df.values.tolist(), columns=df.columns)

# # Step 3: Change first column from text to number
# df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

# # Step 4: Replace errors into null
# df = df.replace({'ERROR': pd.NA})

# # Step 5: Fill down the value for specific column (e.g., 'column_name')
# df.iloc[:, 0].fillna(method='ffill', inplace=True)

# # Step 6: Fill down the value in the second column until a different name appears
# current_index = df.iloc[0, 0]
# current_name = df.iloc[0, 1]
# for i in range(1, len(df)):
#     if pd.isna(df.iloc[i, 1]):
#         df.iloc[i, 1] = current_name
#     elif df.iloc[i, 0] != current_index:
#         current_index = df.iloc[i, 0]
#         current_name = df.iloc[i, 1]
#     else:
#         continue

# # Step 7: Filter the rows based on a condition (e.g., filter rows where a specific column value is not null)
# df = df[df.iloc[:, 1].notnull()]
# df = df.iloc[7:75]
# df.drop(df.columns[6], axis=1, inplace=True)

# # Step 8: Extract Deductor Name and TAN Number from the DataFrame
# deductor_name = df.iloc[0, 1]
# tan_number = df.iloc[1, 1]

# # Step 9: Add Deductor Name and TAN Number as new columns to the DataFrame
# df.insert(9, 'Deductor Name', deductor_name)
# df.insert(10, 'TAN Number', tan_number)

# # Step 10: Write the modified DataFrame to an Excel file
# # df.to_excel('output_file4.xlsx', index=False, header=False)

# # Step 11: Print Deductor Name and TAN Number
# print("Deductor Name:", deductor_name)
# print("TAN Number:", tan_number)

# # first_cell_values = []
# # current_first_cell_value = df.iloc[0, 0]
# # for i in range(len(df)):
# #     if df.iloc[i, 1] != current_name:
# #         current_name = df.iloc[i, 1]
# #         current_first_cell_value = df.iloc[i, 0]
# #     first_cell_values.append(current_first_cell_value)
# # df.insert(2, 'First Cell Value', first_cell_values)
# current_name_column = df.iloc[0, 2]
# for index, row in df.iterrows():
#     if row[0] != "Sr. No." and row[2] == current_name_column:
#         print(row[2])
#     elif row[0] != "Sr. No." and row[2] != current_name_column:
#         current_name_column = row[2]
#         print(current_name_column)
# df.to_excel('output_file.xlsx', index=False, header=False)

# -----------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
with open("C:/Users/hp/OneDrive/Desktop/finkeep/AAKPM3407D-2023.txt", "r") as f:
  # Convert sample text to a list of lines.
  lines = f.readlines()

  # Initialize variables to store the extracted data.
  deductor_info = {}
  transactions = []

  # Parse the lines.
  for line in lines:
      # Split the line by '^' delimiter and filter out empty strings.
      parts = [part for part in line.split('^') if part]

      # If the line contains 'PART-I - Details of Tax Deducted at Source', it's the start of a new deductor.
      if 'PART-I - Details of Tax Deducted at Source' in line:
          deductor_info = {}  # Reset for the new deductor section.
      elif 'Sr. No.' in line and 'Name of Deductor' in line:
          # This line contains the headers for deductor information, skip it.
          continue
      elif 'Sr. No.' in line and 'Section' in line:
          # This line contains the headers for transaction information, skip it.
          continue
      elif 'File Creation Date' in line:
          # This line is the header line for the file, skip it.
          continue
      elif len(parts) == 13:
          # This line contains file creation info, skip it.
          continue
      elif len(parts) == 7 and parts[0].isdigit():
          # This line contains deductor info.
          deductor_info['Name of Deductor'] = parts[1]
          deductor_info['TAN of Deductor'] = parts[2]
      elif len(parts) > 7 and parts[0].isdigit():
          # This line contains transaction info.
          #print(parts)
          transaction = {
              'Section': parts[1],
              'Transaction Date': parts[2],
              'Status of Booking': parts[3],
              'Date of Booking': parts[4],
              'Amount Paid / Credited (Rs.)': parts[6],
              'Tax Deducted (Rs.)': parts[7],
              'TDS Deposited (Rs.)': parts[8],
              'Name of Deductor': deductor_info.get('Name of Deductor', ''),
              'TAN of Deductor': deductor_info.get('TAN of Deductor', '')
          }
          transactions.append(transaction)

  # Now we create a DataFrame from the transactions list.
  df = pd.DataFrame(transactions)
df.to_excel('final_output_excel.xlsx', index=False, header=False)
print(df)







