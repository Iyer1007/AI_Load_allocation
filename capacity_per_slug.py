import os
import pandas as pd

def get_shipment_counts_for_user(file_path, userid):
    # Initialize an empty dataframe to store combined data
    combined_df = pd.read_csv(file_path)

    # Iterate over each file in the folder
   
    # Filter data for the specified user
    user_df = combined_df[combined_df['user_id'] == userid]

    # Group the data by slug and count the number of packages assigned to each slug by the user
    shipment_counts = user_df.groupby('slug').size().reset_index(name='shipment_count')

    return shipment_counts
