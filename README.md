# 🧾 Consulta de serviços por Cliente (Arquivo .txt)

Este projeto permite consultar o valor total gasto por clientes (CPF, CNPJ ou Nome/Razão Social) a partir de um arquivo `.txt` com estrutura fixa (o arquivo precisa ser igual ao "exemplo_de.txt".

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
