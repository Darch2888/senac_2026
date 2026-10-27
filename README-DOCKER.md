# 🐳 Docker Setup - Senac 2026

## 🚀 Comandos Rápidos

```bash
# Iniciar todos os serviços
docker compose up -d

# Ver status dos containers
docker compose ps

# Executar um exercício Python
docker compose exec python python3 7/7-1.py

# Entrar no container Python (modo interativo)
docker compose exec python bash

# Parar todos os serviços
docker compose down

# Parar e remover volumes (dados serão perdidos)
docker compose down -v
```

---

## 📊 MySQL Workbench - Conexão

**Instale o MySQL Workbench na sua máquina local:**

- Linux: `sudo apt install mysql-workbench`
- Windows: [Download oficial](https://dev.mysql.com/downloads/workbench/)
- Mac: `brew install --cask mysql-workbench`

### Configuração da Conexão

| Campo | Valor |
|-------|-------|
| **Connection Name** | Senac Docker |
| **Hostname** | `127.0.0.1` |
| **Port** | `3306` |
| **Username** | `senac_user` |
| **Password** | `senac123` |
| **Default Schema** | `senac_db` |

### Conectar como ROOT

| Campo | Valor |
|-------|-------|
| **Username** | `root` |
| **Password** | `root123` |

---

## 🗄️ Banco de Dados Criado

### Tabelas Populadas:

- **alunos** - 8 alunos com notas e médias (exercícios condicionais)
- **produtos** - 8 produtos com preços e estoque (exercícios loops/lists)
- **livros** - 5 livros (exercícios strings)
- **numeros** - 5 conjuntos de números (exercícios matemáticos)

### Views Criadas:

- `vw_alunos_aprovados`
- `vw_alunos_reprovados`
- `vw_produtos_estoque_baixo`

### Stored Procedure:

- `sp_atualizar_media(id_aluno)` - Atualiza média e situação do aluno

---

## 🐍 Exemplos de Conexão Python

```python
import pymysql

# Conexão com o banco
conexao = pymysql.connect(
    host='mysql',
    user='senac_user',
    password='senac123',
    database='senac_db'
)

cursor = conexao.cursor()

# Exemplo: listar alunos aprovados
cursor.execute("SELECT * FROM vw_alunos_aprovados")
resultados = cursor.fetchall()

for aluno in resultados:
    print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Média: {aluno[3]}")

conexao.close()
```

---

## 📁 Estrutura Criada

```
senac_2026/
├── docker-compose.yml      # Orquestração dos containers
├── Dockerfile              # Imagem Python customizada
├── requirements.txt        # Dependências Python
├── init-db.sql            # Script de criação do banco
└── README-DOCKER.md       # Este arquivo
```

---

## 🔧 Troubleshooting

**Container MySQL não inicia:**
```bash
docker-compose down -v
docker-compose up -d
```

**Ver logs do MySQL:**
```bash
docker-compose logs mysql
```

**Recriar o banco do zero:**
```bash
docker-compose down -v
docker-compose up -d
```
