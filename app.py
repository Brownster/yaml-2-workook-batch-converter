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
            yaml_file_path = os.path.join(yaml_folder, filename)
            csv_file_name = filename.rsplit('.', 1)[0] + '.csv'
            csv_file_path = os.path.join(output_folder, csv_file_name)

            try:
                print(f"Converting {yaml_file_path} to {csv_file_path}")
                yaml_to_csv(yaml_file_path, csv_file_path)

                # Process commented-out targets
                modified_yaml_file_path = process_commented_targets(yaml_file_path)
                modified_csv_file_name = filename.rsplit('.', 1)[0] + '_hashed_targets.csv'
                modified_csv_file_path = os.path.join(output_folder, modified_csv_file_name)

                print(f"Converting commented targets in {modified_yaml_file_path} to {modified_csv_file_path}")
                yaml_to_csv(modified_yaml_file_path, modified_csv_file_path)

            except Exception as e:
                print(f"Failed to convert {yaml_file_path}: {e}")
                failed_files.append(yaml_file_path)

        else:
            print(f"Skipping {filename}, not a YAML file.")

    # Print the list of failed files
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