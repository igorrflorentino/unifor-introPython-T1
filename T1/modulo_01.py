import os, csv, re
from gdown import download
from matplotlib.pyplot import inferno


def get_gdrive_file_ID(link) -> str:
    """
    get the file ID from a google drive link
    it allows the following links format:
    - https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9/view?usp=sharing
    - https://drive.google.com/open?id=1A2B3C4D5E6F7G8H9
    :param link: google drive link
    :return: file ID
    """
    # search for the expression '/d/' or 'id=' and then capture all chars until it finds '/' or '&'
    print("parsing google drive link")
    regex = r"(?:/d/|id=)([^/&]+)"
    result = re.search(regex, link)
    print(f"google drive file ID aquired: {result.group(1)}")
    return result.group(1) if result else ""

def download_dataset(link,filename) -> str:
    """
    downloads the dataset from google drive
    :param link: google drive link of the file
    :param filename: name of the file to be saved
    :return: no return
    """
    print("fetching google drive file")
    file_id = get_gdrive_file_ID(link)
    download(id=file_id, output=filename)
    print("google drive file saved at:", filename)
    return filename

def preencher_matriz_contratos(nome_arquivo: str) -> tuple[int, int, float, list[list[list[float]]]]:
    print("building the contracts matrix")
    with open(nome_arquivo, 'r') as file:
        for index, line in enumerate(file):
            #getting the metadados and initiating the matix
            if index == 0:
                metadados = line.strip().split()
                if len(metadados) == 3:
                    longger_contract_term = int(metadados[0])
                    suppliers_count = int(metadados[1])
                    change_fee = float(metadados[2])
                    matriz_contratos = [[["---"] * (longger_contract_term + 1) for _ in range(longger_contract_term + 1)]  for supplier in range(suppliers_count + 1)]
                else:
                    raise ValueError("Metadados invalidos na primeira linha do arquivo")
            # filling the matix
            else:
                data = line.strip().split()
                if len(data) == 4:
                    supplier_ID = int(data[0])
                    start_contract_term = int(data[1])
                    end_contract_term = int(data[2])
                    contract_value = float(data[3])
                    matriz_contratos[supplier_ID][start_contract_term][end_contract_term] = contract_value
                else:
                    raise ValueError(f"Dados incompletos na linha {index} do arquivo")

    print(f"final matrix constructed: {len(matriz_contratos)}x{len(matriz_contratos[0])}x{len(matriz_contratos[0][0])}")
    return longger_contract_term, suppliers_count, change_fee, matriz_contratos

def imprimir_matriz(matriz, k=None):
    print("printing the matrix")
    if k is None:
        print("no supplier selected, printing the whole matrix")
        # Imprimir toda a matriz
        for fornecedor, submatriz in enumerate(matriz):
            print(f"Fornecedor {fornecedor}:")
            for linha in submatriz:
                print(" ".join(map(str, linha)))
            print()  # Linha em branco para separar fornecedores
    else:
        print("supplier selected, printing only that one")
        # Verificar se o índice está dentro do intervalo
        if k < 0 or k >= len(matriz):
            print("Error: invalid supplier .")
            return
        # Imprimir apenas o fornecedor k
        print(f"Fornecedor {k}:")
        for linha in matriz[k]:
            print(" ".join(map(str, linha)))

def exportar_csv(nome_arquivo, matriz):
    print("exporting the matrix to csv")
    with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for i, supplier in enumerate(matriz):
            escritor.writerow([f"Fornecedor {i}"])  # Adiciona um cabeçalho para cada plano
            escritor.writerows(supplier)
            escritor.writerow([])  # Linha em branco entre planos
    print(f"Matriz exportada com sucesso para {nome_arquivo}")