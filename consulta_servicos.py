import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def buscar_cliente_em_arquivo(caminho, consulta):
    resultados = []
    soma = 0
    quantidade = 0

    with open(caminho, "r", encoding="latin1") as f:
        for linha in f:
            if linha.startswith("2RPS"):
                doc = linha[73:87].strip()
                nome = linha[107:181].strip()
                valor_str = linha[32:47].strip()
                recibo = linha[17:23].strip()
                data_str = linha[23:31].strip()

                # Converte data AAAAMMDD -> DD/MM/AAAA
                try:
                    data_formatada = datetime.strptime(data_str, "%Y%m%d").strftime("%d/%m/%Y")
                except:
                    data_formatada = data_str

                if consulta.lower() in nome.lower() or consulta in doc:
                    try:
                        valor = int(valor_str)
                        soma += valor
                        quantidade += 1
                        resultados.append((recibo, data_formatada, nome, doc, valor / 100))
                    except:
                        pass
    return resultados, soma, quantidade

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
    resultados, total, quantidade = buscar_cliente_em_arquivo(caminho, consulta)
    saida.delete("1.0", tk.END)
    if resultados:
        for recibo, data, nome, doc, valor in resultados:
            saida.insert(tk.END, "Recibo ")
            saida.insert(tk.END, recibo, "recibo")  # destacado
            saida.insert(tk.END, f" | Data: {data} | {nome} ({doc}) | Valor: ")
            saida.insert(tk.END, f"R$ {valor:,.2f}", "valor")  # destacado
            saida.insert(tk.END, "\n")
        saida.insert(tk.END, f"\n🧾 Quantidade de serviços: {quantidade}\n")
        saida.insert(tk.END, f"💰 Total gasto: R$ {total / 100:,.2f}\n", "valor")
    else:
        saida.insert(tk.END, "Nenhum resultado encontrado.")

# Interface
janela = tk.Tk()
janela.title("Consulta de Gastos por Cliente")
janela.geometry("980x600")

tk.Label(janela, text="Arquivo .txt:").pack(pady=2)
entrada_arquivo = tk.Entry(janela, width=60)
entrada_arquivo.pack()
tk.Button(janela, text="Selecionar arquivo", command=procurar_arquivo).pack(pady=4)

tk.Label(janela, text="Nome ou CNPJ:").pack(pady=2)
entrada_cliente = tk.Entry(janela, width=60)
entrada_cliente.pack()

tk.Button(janela, text="Buscar", command=executar_busca, bg="#4CAF50", fg="white").pack(pady=10)

saida = tk.Text(janela, height=25, width=120)
saida.pack()

# Definição de estilos (tags)
saida.tag_config("recibo", foreground="green", font=("Abadi", 10, "bold"))
saida.tag_config("valor", foreground="green", font=("Abadi", 10, "bold"))

janela.mainloop()

