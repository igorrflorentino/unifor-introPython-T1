from T1 import download_dataset
from T1 import preencher_matriz_contratos
from T1 import imprimir_matriz
from T1 import exportar_csv
import os

def main():

    # creating folder structure
    input_file_name = "dataset"
    input_folder_name = "inputs"
    output_file_name = "dataframe.csv"
    output_folder_name = "outputs"

    project_folder_path = os.path.abspath("")
    input_folder_path = os.path.join(project_folder_path, input_folder_name)
    output_folder_path = os.path.join(project_folder_path, output_folder_name)

    os.makedirs(input_folder_path, exist_ok=True)
    os.makedirs(output_folder_path, exist_ok=True)

    input_file_path = os.path.join(input_folder_path, input_file_name)
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Download do dataset
    # link_txt = "https://drive.google.com/file/d/1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_/view?usp=drive_link"
    link_txt = "https://drive.google.com/file/d/17KOe8bJvHDceTpGZ9ru1YvjlROIMWhZ3/view?usp=drive_link"

    download_dataset(link_txt,input_file_path)

    # Preencher a matriz de contratos
    _, _, _, matriz = preencher_matriz_contratos(input_file_path)
    
    # Imprimir os resultados
    imprimir_matriz(matriz, 1)

    # Exportar a matriz de contratos
    exportar_csv(output_file_path, matriz)
    
if __name__ == "__main__":
    main()