# Verificador de Senhas Fracas

Este projeto permite verificar senhas fracas em massa a partir de um arquivo `.csv`, comparando-as com a base de dados comprometidos da API HaveIBeenPwned.

## Funcionalidades

- Leitura de senhas de um CSV
- Verificação via SHA-1 usando a API pública HaveIBeenPwned (k-anonymity)
- Geração de relatório com senhas comprometidas
- CLI interativa

## Instalação

```bash
pip install -r requirements.txt
Como usar
bash
Copy
Edit
python main.py --arquivo data/senhas.csv --modo sha1
Modos disponíveis:

sha1: compara hashes SHA-1 com a base pública de senhas vazadas.

brute: simula força bruta em senhas fracas (limitado e didático).

Estrutura
verificador/: Lógica principal do sistema

data/: Arquivo de senhas para teste

reports/: Relatórios de senhas encontradas

yaml
Copy
Edit

---

### ✅ `data/senhas.csv`
```csv
senha
123456
admin
senha123
letmein
qwerty