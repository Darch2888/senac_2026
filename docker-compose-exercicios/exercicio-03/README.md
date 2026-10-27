# 📝 Exercício 3: Volumes e Persistência de Dados

## 🎯 Objetivo

Aprender a **persistir dados** usando volumes Docker e bind mounts.

---

## 📋 Conceitos Novos

### Tipos de Volumes

| Tipo | Sintaxe | Descrição | Uso |
|------|---------|-----------|-----|
| **Named Volume** | `nome_volume:/caminho` | Gerenciado pelo Docker | Dados do banco |
| **Bind Mount** | `./local:/container` | Arquivo do host → Container | Código, configs |
| **Anonymous** | `/caminho` | Sem nome, temporário | Cache, tmp |

### Quando usar cada um?

- **Named Volume:** Dados que precisam persistir (bancos de dados)
- **Bind Mount:** Arquivos de desenvolvimento (código, HTML)
- **Anonymous:** Dados temporários (cache)

---

## 🏗️ Arquivo Explicado

```yaml
volumes:
  # Named volume - Docker gerencia onde fica
  - db_data:/var/lib/mysql

  # Bind mount - caminho relativo do projeto
  - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  # Bind mount - edição em tempo real
  - ./html:/usr/share/nginx/html
```

---

## 🚀 Passo a Passo

### Passo 1: Entre no diretório

```bash
cd docker-compose-exercicios/exercicio-03/
```

### Passo 2: Veja os arquivos locais

```bash
ls -la
# Temos: docker-compose.yml, init.sql, html/
```

### Passo 3: Suba os containers

```bash
docker-compose up -d
```

### Passo 4: Acesse o site

Abra: http://localhost:8080

Você verá a página HTML do `html/index.html`

### Passo 5: Edite o arquivo em tempo real

```bash
# Edite o HTML com nano ou seu editor
nano html/index.html

# Mude o título, salve, e atualize o navegador
# A mudança aparece instantaneamente!
```

### Passo 6: Verifique o banco foi inicializado

```bash
docker-compose exec database mysql -uwp_user -pwp123 wordpress -e "SELECT * FROM teste;"
```

### Passo 7: Veja onde os volumes estão no host

```bash
docker volume inspect exercicio-03_db_data
```

### Passo 8: Teste a persistência do banco

```bash
# Adicione dados no banco
docker-compose exec database mysql -uwp_user -pwp123 wordpress \
  -e "INSERT INTO teste (mensagem) VALUES ('Dado novo!');"

# Pare os containers
docker-compose down

# Suba novamente
docker-compose up -d

# Verifique que o dado ainda está lá!
docker-compose exec database mysql -uwp_user -pwp123 wordpress \
  -e "SELECT * FROM teste;"
```

### Passo 9: Limpe tudo (incluindo volumes)

```bash
docker-compose down -v
```

Agora sim, tudo foi removido.

---

## ✅ Checklist

- [ ] Entendeu diferença entre Named Volume e Bind Mount
- [ ] Editou HTML e viu mudanças instantâneas
- [ ] Viu que o banco persiste após `docker-compose down`
- [ ] Usou `docker volume inspect` para ver localização
- [ ] Testou `docker-compose down -v` para limpar volumes

---

## 🤔 Questões para Reflexão

1. Por que usamos `./html:/usr/share/nginx/html` para desenvolvimento?
2. Quando você deve usar Named Volume ao invés de Bind Mount?
3. O que acontece com os dados se você esquecer o `-v` ao dar `docker-compose down`?

---

## 🎯 Desafios

### Desafio 1: Criar um arquivo de logs

Adicione um volume para logs que persista:

```yaml
  app:
    volumes:
      - ./logs:/var/log/nginx
      # ... outros volumes
```

```bash
mkdir logs
docker-compose restart app
# Acesse o site várias vezes
ls logs/
```

### Desafio 2: Backup do volume

```bash
# Fazer backup do volume
docker run --rm -v exercicio-03_db_data:/data -v $(pwd):/backup \
  alpine tar czf /backup/db-backup.tar.gz /data

# Testar: apague volume e restaure
docker-compose down -v
docker volume rm exercicio-03_db_data

# Restaurar
docker run --rm -v exercicio-03_db_data:/data -v $(pwd):/backup \
  alpine tar xzf /backup/db-backup.tar.gz -C /
```

---

## 📚 Comandos Novos

| Comando | O que faz |
|---------|-----------|
| `docker volume ls` | Lista volumes |
| `docker volume inspect nome` | Detalhes do volume |
| `docker-compose down -v` | Remove containers E volumes |
| `docker run --rm -v volume:/data` | Acessa volume de outro container |

---

## 📊 Diagrama dos Volumes

```
┌─────────────────────────────────────────────────────────┐
│                      HOST                               │
│                                                         │
│  ./html/index.html  ──Bind Mount──→  /usr/share/nginx  │
│                                                         │
│  ./init.sql        ──Bind Mount──→  /docker-entrypoint │
│                                                         │
│  /var/lib/docker/volumes/    ──Named──→  /var/lib/mysql│
│  exercicio-03_db_data/_data                          │
└─────────────────────────────────────────────────────────┘
```

---

## ➡️ Próximo Exercício

Quando terminar, vá para: `../exercicio-04/`
