from T1 import (
    extract_gdrive_file_id,
    download_gdrive_file,
    build_contracts_matrix,
    print_matrix,
    export_csv
)
import os

def main():
    """
    Main function to execute the contract matrix workflow:
    - Create folder structure
    - Download the dataset
    - Populate the contracts matrix
    - Print and export the results
    """

    # Defining folder and file names
    input_file_name = "dataset"
    input_folder_name = "inputs"
    output_file_name = "dataframe.csv"
    output_folder_name = "outputs"

    # Creating folder structure
    project_folder_path = os.path.abspath("")
    input_folder_path = os.path.join(project_folder_path, input_folder_name)
    output_folder_path = os.path.join(project_folder_path, output_folder_name)

    os.makedirs(input_folder_path, exist_ok=True)
    os.makedirs(output_folder_path, exist_ok=True)

    # Defining file paths
    input_file_path = os.path.join(input_folder_path, input_file_name)
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Download the dataset
    # link_txt = "https://drive.google.com/file/d/1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_/view?usp=drive_link"
    link_txt = "https://drive.google.com/file/d/17KOe8bJvHDceTpGZ9ru1YvjlROIMWhZ3/view?usp=drive_link"
    download_gdrive_file(link_txt, input_file_path)

    # Populate the contracts matrix
    longest_contract_term, suppliers_count, change_fee, contracts_matrix = build_contracts_matrix(input_file_path)

    # Print the results
    print(f"m:{longest_contract_term} n:{suppliers_count} t:{change_fee}")
    print_matrix(contracts_matrix, supplier_id=1)

    # Export the contracts matrix
    export_csv(output_file_path, contracts_matrix)

if __name__ == "__main__":
    main()