import pandas as pd
import os

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

new_df = pd.DataFrame({
    'Name' : ['John'],
    'Age' : [45],
    'City' : ['Indiana']
})

df = pd.concat([df, new_df], ignore_index = True)

# creating data directory

data_dir = './data'
os.makedirs(data_dir, exist_ok = True)

file_path = os.path.join(data_dir, 'data.csv')

df.to_csv(file_path, index = False)
print(f"csv file saved to {file_path}")