import csv

def filter_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as input_csv, open(output_file, 'w', newline='') as output_csv:
        reader = csv.DictReader(input_csv)
        writer = csv.DictWriter(output_csv, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            if len(row['destpin']) >= 6:  # Checking if 'destpin' has at least 6 characters
                writer.writerow(row)

# Example usage:
input_file_path = 'D:\Eshipz\AI_LOAD_DATA\CODE\merged_data.csv'  # Provide the path to your input CSV file
output_file_path = 'D:\Eshipz\AI_LOAD_DATA\CODE\data.csv'  # Provide the path to your output CSV file

filter_csv(input_file_path, output_file_path)
print("Filtered CSV created successfully.")
