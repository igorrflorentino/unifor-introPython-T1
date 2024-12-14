import os, csv, re
from gdown import download

def extract_gdrive_file_id(link: str) -> str:
    """
    Extract the file ID from a Google Drive link.

    This function supports the following link formats:
    - https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9/view?usp=sharing
    - https://drive.google.com/open?id=1A2B3C4D5E6F7G8H9

    :param link: A valid Google Drive link
    :return: The extracted file ID if found, otherwise an empty string
    """
    print("Parsing Google Drive link...")
    regex = r"(?:/d/|id=)([^/&]+)"  # Match '/d/' or 'id=' and capture the following characters until '/' or '&'
    match = re.search(regex, link)

    if match:
        file_id = match.group(1)
        print(f"Google Drive file ID extracted successfully: {file_id}")
        return file_id
    else:
        print("Failed to extract Google Drive file ID.")
        return ""


def download_gdrive_file(link: str, filename: str) -> str:
    """
    Download a dataset from Google Drive.

    :param link: The Google Drive link of the file.
    :param filename: The name of the file to be saved locally.
    :return: The path to the saved file.
    """
    print("Fetching Google Drive file...")

    # Extract the file ID from the provided link
    file_id = extract_gdrive_file_id(link)

    if file_id:
        # Download the file using the extracted file ID
        download(id=file_id, output=filename)
        print(f"Google Drive file saved at: {filename}")
        return filename
    else:
        raise ValueError("Invalid Google Drive link. File ID could not be extracted.")


def build_contracts_matrix(filename: str) -> (int, int, float, [[[float]]]):
    """
    Builds the contracts matrix based on data from a file.

    :param filename: Name of the input file containing metadata and contract data.
    :return: A tuple containing:
             - The longest contract term (int).
             - The number of suppliers (int).
             - The change fee (float).
             - The contracts matrix (3D list of floats).
    """
    print("Building the contracts matrix...")

    with open(filename, 'r') as file:
        for index, line in enumerate(file):
            # Parse metadata and initialize the matrix
            if index == 0:
                metadata = line.strip().split()
                if len(metadata) == 3:
                    longest_contract_term = int(metadata[0])
                    suppliers_count = int(metadata[1])
                    change_fee = float(metadata[2])
                    contracts_matrix = [
                        [["---"] * (longest_contract_term + 1) for _ in range(longest_contract_term + 1)]
                        for _ in range(suppliers_count + 1)
                    ]
                else:
                    raise ValueError("Invalid metadata in the first line of the file.")
            # Populate the matrix with contract data
            else:
                data = line.strip().split()
                if len(data) == 4:
                    supplier_id = int(data[0])
                    start_term = int(data[1])
                    end_term = int(data[2])
                    contract_value = float(data[3])
                    contracts_matrix[supplier_id][start_term][end_term] = contract_value
                else:
                    raise ValueError(f"Incomplete data on line {index + 1} of the file.")

    print(f"Final matrix dimensions: {len(contracts_matrix)}x{len(contracts_matrix[0])}x{len(contracts_matrix[0][0])}")
    return longest_contract_term, suppliers_count, change_fee, contracts_matrix


def print_matrix(matrix, supplier_id=None):
    """
    Prints the contract matrix. If a specific supplier is selected, only that supplier's data is printed.

    :param matrix: The 3D matrix containing contract data.
    :param supplier_id: The index of the supplier to print (optional).
    """
    print("Printing the matrix...")

    if supplier_id is None:
        print("No supplier selected, printing the entire matrix.")
        # Print the entire matrix
        for supplier, submatrix in enumerate(matrix):
            print(f"Supplier {supplier}:")
            for row in submatrix:
                print(" ".join(map(str, row)))
            print()  # Blank line to separate suppliers
    else:
        print(f"Supplier selected: {supplier_id}. Printing only this supplier.")
        # Check if the supplier index is valid
        if supplier_id < 0 or supplier_id >= len(matrix):
            print("Error: Invalid supplier ID.")
            return
        # Print only the specified supplier's data
        print(f"Supplier {supplier_id}:")
        for row in matrix[supplier_id]:
            print(" ".join(map(str, row)))

def export_csv(filename: str, matrix: list):
    """
    Exports the contract matrix to a CSV file.

    :param filename: The name of the CSV file to save the matrix.
    :param matrix: The 3D matrix containing contract data.
    """
    print("Exporting the matrix to CSV...")

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for i, supplier in enumerate(matrix):
            writer.writerow([f"Supplier {i}"])  # Add a header for each supplier
            writer.writerows(supplier)
            writer.writerow([])  # Blank line between suppliers

    print(f"Matrix successfully exported to {filename}")