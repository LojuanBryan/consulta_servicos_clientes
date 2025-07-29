# 🧾 Consulta de serviços por Cliente (Arquivo .txt)

Este projeto permite consultar o valor total gasto por clientes (CPF, CNPJ ou Nome/Razão Social) a partir de um arquivo `.txt` com estrutura fixa (o arquvivo precisa ser igual ao "exemplo_de.txt".

Você pode utilizar de duas formas:

---

## 🟩 OPÇÃO 1 — Interface no Google Colab (online)

### ✅ Vantagens:
- Não precisa instalar nada
- Interface simples via navegador
- Ideal para uso pessoal ou testes rápidos

### ▶️ Como usar:
1. Acesse o consulta_gastos_clientes.ipynb no Google Colab.
2. Faça upload do arquivo `.txt` clicando no botão de upload
3. Digite o nome, CPF ou CNPJ do cliente
4. O notebook mostrará:
   - Lista de serviços realizados
   - Total gasto pelo cliente no período

---

## 🟦 OPÇÃO 2 — Aplicativo Desktop com Tkinter (offline)

### ✅ Vantagens:
- Interface de janela simples (sem terminal)
- Pode virar `.exe` e ser distribuído para qualquer pessoa
- Funciona mesmo sem internet

### ▶️ Como usar:

#### A) Com Python instalado:
1. Instale o Python (https://www.python.org/downloads/)
2. Salve o arquivo `consulta_clientes.py` na sua máquina
3. Rode com duplo clique ou pelo terminal:
   ```bash
   python consulta_clientes.py

#### B) Criando um .exe (para colegas que não têm Python):
1.Instale o PyInstaller:
2. Gere o .exe
pyinstaller --onefile --windowed consulta_clientes.py
3. O executável estará na pasta dist/
4. Compartilhe o .exe com seus colegas (pasta de rede, pendrive, etc.)

📄 Estrutura esperada do arquivo .txt:
Linhas com serviços começam com 2RPS

Valor gasto está nas posições 33 a 47 (15 dígitos, ex: 000000000530340 = R$ 5.303,40)

CPF/CNPJ está nas posições 74 a 87

Nome/Razão Social nas posições 108 a 181



✍️ Autor
Desenvolvido por Lojuan Bryan com apoio do ChatGPT.
