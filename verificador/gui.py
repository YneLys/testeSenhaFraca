import tkinter as tk
from tkinter import filedialog, messagebox
from verificador.checker import verificar_sha1, verificar_brute

def selecionar_arquivo():
    caminho = filedialog.askopenfilename(title="Selecionar CSV", filetypes=[("CSV files", "*.csv")])
    if caminho:
        entry_arquivo.delete(0, tk.END)
        entry_arquivo.insert(0, caminho)

def executar_verificacao():
    caminho = entry_arquivo.get().strip()
    modo = var_modo.get()

    if not caminho:
        messagebox.showwarning("Erro", "Selecione um arquivo CSV.")
        return

    try:
        if modo == "sha1":
            verificar_sha1(caminho)
        else:
            verificar_brute(caminho)
        messagebox.showinfo("Finalizado", f"Verificação concluída com sucesso. Relatório salvo em /reports.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")

# Interface
janela = tk.Tk()
janela.title("Verificador de Senhas Fracas")
janela.geometry("420x250")

tk.Label(janela, text="Arquivo CSV de Senhas:").pack(pady=5)
frame = tk.Frame(janela)
frame.pack()

entry_arquivo = tk.Entry(frame, width=40)
entry_arquivo.pack(side=tk.LEFT, padx=5)
btn_browse = tk.Button(frame, text="Procurar", command=selecionar_arquivo)
btn_browse.pack(side=tk.LEFT)

tk.Label(janela, text="Modo de Verificação:").pack(pady=10)

var_modo = tk.StringVar(value="sha1")
tk.Radiobutton(janela, text="SHA-1 (API HaveIBeenPwned)", variable=var_modo, value="sha1").pack()
tk.Radiobutton(janela, text="Brute Force (Dicionário)", variable=var_modo, value="brute").pack()

tk.Button(janela, text="Executar Verificação", command=executar_verificacao).pack(pady=20)

janela.mainloop()
