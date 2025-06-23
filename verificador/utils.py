import os
from datetime import datetime

def salvar_relatorio(lista_senhas, modo):
    if not lista_senhas:
        print("Nenhuma senha comprometida encontrada.")
        return

    os.makedirs("reports", exist_ok=True)
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho = f"reports/relatorio_{modo}_{data}.txt"

    with open(caminho, "w") as f:
        f.write("Senhas comprometidas encontradas:\n")
        for senha in lista_senhas:
            f.write(f"{senha}\n")

    print(f"Relatório salvo em: {caminho}")
