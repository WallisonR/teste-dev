import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from zipfile import ZipFile

# Caminho para o ChromeDriver (ajuste conforme sua instalação)
chrome_driver_path = 'C:/Users/user/teste-dev/web_scraping/chromedriver-win64/chromedriver.exe'  # Atualize com o caminho correto

# URL do site
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-dasociedade/atualizacao-do-rol-de-procedimentos'

# Função para baixar o arquivo PDF
def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo baixado com sucesso: {save_path}")
    else:
        print(f"Falha no download do arquivo: {pdf_url}")

# Função para fazer o scraping da página e extrair os links dos PDFs
def get_pdf_links_selenium(page_url):
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(page_url)
        wait = WebDriverWait(driver, 10)

        # Aguardar carregamento da página e garantir que todos os links sejam encontrados
        time.sleep(5)

        pdf_links = []
        elements = driver.find_elements(By.TAG_NAME, 'a')

        for element in elements:
            try:
                link = element.get_attribute('href')
                if link and 'pdf' in link:
                    pdf_links.append(link)
            except Exception as e:
                print(f"Erro ao acessar elemento: {e}")

        return pdf_links
    except Exception as e:
        print(f"Erro ao obter links de PDF: {e}")
        return []
    finally:
        driver.quit()

# Função para compactar os arquivos em um ZIP
def compress_pdfs(pdf_files, zip_name):
    with ZipFile(zip_name, 'w') as zipf:
        for pdf in pdf_files:
            zipf.write(pdf, os.path.basename(pdf))
        print(f"Arquivos compactados em: {zip_name}")

# Função principal
def main():
    if not os.path.exists('dados'):
        os.makedirs('dados')

    pdf_links = get_pdf_links_selenium(url)
    
    if not pdf_links:
        print("Nenhum link de PDF encontrado.")
        return

    pdf_paths = []
    for idx, link in enumerate(pdf_links):
        pdf_filename = f"Anexo-{idx+1}.pdf"
        pdf_path = os.path.join('dados', pdf_filename)
        download_pdf(link, pdf_path)
        pdf_paths.append(pdf_path)
    
    compress_pdfs(pdf_paths, 'anexos.zip')

if __name__ == "__main__":
    main()
