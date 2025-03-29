import os
from zipfile import ZipFile

def compress_pdfs(folder, zip_name):
    pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado para compactação.")
        return

    with ZipFile(zip_name, 'w') as zipf:
        for pdf in pdf_files:
            pdf_path = os.path.join(folder, pdf)
            zipf.write(pdf_path, pdf)  # Adiciona o arquivo ao ZIP
        print(f"{len(pdf_files)} arquivos compactados em: {zip_name}")

def main():
    folder = 'dados'
    if not os.path.exists(folder):
        print(f"A pasta '{folder}' não existe. Nenhum arquivo para compactar.")
        return

    compress_pdfs(folder, 'anexos.zip')

if __name__ == "__main__":
    main()
