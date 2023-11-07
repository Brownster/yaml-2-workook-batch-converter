import os
import sys
from importer import yaml_to_csv

def bulk_yaml_to_csv(yaml_folder, output_folder):
    # Check if output_folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List to keep track of failed files
    failed_files = []

    # Iterate through each file in the directory
    for filename in os.listdir(yaml_folder):
        # Check if the file is a YAML file
        if filename.endswith('.yaml') or filename.endswith('.yml') or filename.endswith('.eyaml'):
            # Construct full file paths
            yaml_file_path = os.path.join(yaml_folder, filename)
            # Create a proper CSV filename
            csv_file_name = filename.rsplit('.', 1)[0] + '.csv'  # Replace YAML extension with CSV
            csv_file_path = os.path.join(output_folder, csv_file_name)

            try:
                # Attempt to convert the YAML file to CSV
                print(f"Converting {yaml_file_path} to {csv_file_path}")
                yaml_to_csv(yaml_file_path, csv_file_path)
            except Exception as e:
                # If an error occurs during conversion, skip the file and print an error message
                print(f"Failed to convert {yaml_file_path}: {e}")
                failed_files.append(yaml_file_path)  # Add the failed file path to the list
        else:
            # If the file is not a YAML file, skip it
            print(f"Skipping {filename}, not a YAML file.")

    # Print the list of failed files at the end
    if failed_files:
        print("\nThe following files failed to convert:")
        for failed_file in failed_files:
            print(failed_file)
    else:
        print("\nAll files converted successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python bulk_yaml_to_csv.py <yaml_folder_path> <output_csv_folder_path>")
        sys.exit(1)

    yaml_folder_path = sys.argv[1]
    output_csv_folder_path = sys.argv[2]

    bulk_yaml_to_csv(yaml_folder_path, output_csv_folder_path)

