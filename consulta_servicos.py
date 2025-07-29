import tkinter as tk
from tkinter import filedialog, messagebox

def buscar_cliente_em_arquivo(caminho, consulta):
    resultados = []
    soma = 0

    with open(caminho, "r", encoding="latin1") as f:
        for linha in f:
            if linha.startswith("2RPS"):
                doc = linha[73:87].strip()
                nome = linha[107:181].strip()
                valor_str = linha[32:47].strip()
                if consulta.lower() in nome.lower() or consulta in doc:
                    try:
                        valor = int(valor_str)
                        resultados.append(f"{nome} ({doc}): R$ {valor / 100:,.2f}")
                        soma += valor
                    except:
                        pass
    return resultados, soma

def procurar_arquivo():
    caminho = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not caminho:
        return
    entrada_arquivo.delete(0, tk.END)
    entrada_arquivo.insert(0, caminho)

def executar_busca():
    caminho = entrada_arquivo.get()
    consulta = entrada_cliente.get()
    if not caminho or not consulta:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return
    resultados, total = buscar_cliente_em_arquivo(caminho, consulta)
    saida.delete("1.0", tk.END)
    if resultados:
        for linha in resultados:
            saida.insert(tk.END, linha + "\n")
        saida.insert(tk.END, f"\nTotal gasto: R$ {total / 100:,.2f}")
    else:
        saida.insert(tk.END, "Nenhum resultado encontrado.")

# Interface
janela = tk.Tk()
janela.title("Consulta de Gastos por Cliente")

tk.Label(janela, text="Arquivo .txt:").pack()
entrada_arquivo = tk.Entry(janela, width=60)
entrada_arquivo.pack()
tk.Button(janela, text="Selecionar arquivo", command=procurar_arquivo).pack()

tk.Label(janela, text="Nome ou CNPJ:").pack()
entrada_cliente = tk.Entry(janela, width=60)
entrada_cliente.pack()

tk.Button(janela, text="Buscar", command=executar_busca).pack()

saida = tk.Text(janela, height=20, width=80)
saida.pack()

janela.mainloop()

