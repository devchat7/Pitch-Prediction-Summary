import pandas as pd
import itertools

# Load the existing predictions CSV (replace 'predictions.csv' with the correct file path)
predictions = pd.read_csv('predictions.csv')

# Define the possible values for balls, strikes, and runners on base
balls = [0, 1, 2, 3]  # Max 3 balls before walk
strikes = [0, 1, 2]    # Max 2 strikes before out
runners_on_base = list(itertools.product([0, 1], repeat=3))  # All combinations of 0 or 1 runner on 1B, 2B, 3B

# Create a list to store the expanded rows
expanded_rows = []

# Iterate over each player in the predictions
for index, row in predictions.iterrows():
    # Iterate over all possible combinations of balls, strikes, and runners on base
    for b, s, (on_1b, on_2b, on_3b) in itertools.product(balls, strikes, runners_on_base):
        # Create a new row for each combination
        expanded_row = row.copy()
        expanded_row['BALLS'] = b
        expanded_row['STRIKES'] = s
        expanded_row['ON_1B'] = on_1b
        expanded_row['ON_2B'] = on_2b
        expanded_row['ON_3B'] = on_3b
        
        # Append the expanded row to the list
        expanded_rows.append(expanded_row)

# Convert the list of expanded rows to a DataFrame
expanded_df = pd.DataFrame(expanded_rows)

# Save the expanded DataFrame to a new CSV file
expanded_df.to_csv('expanded_predictions.csv', index=False)

# Display the first few rows of the expanded DataFrame
print(expanded_df.head())
