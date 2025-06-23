import hashlib
import pandas as pd
import requests
import os

from verificador.utils import salvar_relatorio

def sha1_hash(senha):
    return hashlib.sha1(senha.encode("utf-8")).hexdigest().upper()

def verificar_sha1(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    comprometidas = []

    for senha in df["senha"]:
        hash_senha = sha1_hash(senha)
        prefixo, sufixo = hash_senha[:5], hash_senha[5:]
        resposta = requests.get(f"https://api.pwnedpasswords.com/range/{prefixo}")

        if resposta.status_code == 200:
            if any(sufixo in linha for linha in resposta.text.splitlines()):
                comprometidas.append(senha)
                print(f"[COMPROMETIDA] {senha}")
            else:
                print(f"[SEGURA] {senha}")
        else:
            print("Erro ao acessar a API.")

    salvar_relatorio(comprometidas, "sha1")

def verificar_brute(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo)
    dicionario = ["123456", "admin", "senha", "password", "123456789"]
    comprometidas = [s for s in df["senha"] if s.lower() in dicionario]

    for senha in df["senha"]:
        if senha.lower() in dicionario:
            print(f"[FRACA - DICIONÁRIO] {senha}")
        else:
            print(f"[SEGURA] {senha}")

    salvar_relatorio(comprometidas, "brute")
