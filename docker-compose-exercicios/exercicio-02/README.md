# 📝 Exercício 2: Múltiplos Containers

## 🎯 Objetivo

Trabalhar com **múltiplos containers** que se comunicam através de redes Docker.

---

## 📋 Conceitos Novos

### 1. Múltiplos Serviços

Um arquivo `docker-compose.yml` pode definir vários containers que trabalham juntos.

### 2. Networks (Redes)

- Containers na mesma rede podem se comunicar pelo **nome do serviço**
- `frontend` - serviços públicos (web)
- `backend` - serviços internos (banco)

### 3. depends_on

Define a **ordem de inicio** dos containers.

⚠️ **Importante:** `depends_on` não garante que o serviço está PRONTO, apenas que foi STARTADO.

### 4. Volumes

Persistem dados mesmo quando containers são removidos.

---

## 🏗️ Arquivo Explicado

```yaml
services:
  web:
    depends_on:
      - api              # web só inicia DEPOIS que api iniciar
    networks:
      - frontend         # web está na rede frontend

  api:
    networks:
      - frontend         # api se comunica com web
      - backend         # api se comunica com database

  database:
    environment:         # Variáveis de ambiente do MySQL
      MYSQL_ROOT_PASSWORD: root123
    networks:
      - backend         # database só na rede interna
    volumes:
      - db_data:/var/lib/mysql   # Persiste dados do banco

networks:
  frontend:              # Rede externa
  backend:              # Rede interna (sem acesso externo)

volumes:
  db_data:              # Volume named (persiste após down)
```

---

## 🚀 Passo a Passo

### Passo 1: Entre no diretório

```bash
cd docker-compose-exercicios/exercicio-02/
```

### Passo 2: Suba todos os containers

```bash
docker-compose up -d
```

Você verá:
```
Creating network "exercicio-02_frontend"
Creating network "exercicio-02_backend"
Creating volume "exercicio-02_db_data"
Creating senac_db ...
Creating senac_api ...
Creating senac_web ...
```

### Passo 3: Veja os containers rodando

```bash
docker-compose ps
```

Saída esperada:
```
NAME        SERVICE    STATUS          PORTS
senac_api   api        Up
senac_db    database   Up (healthy)   3306
senac_web   web        Up              0.0.0.0:8080->80/tcp
```

### Passo 4: Veja as redes criadas

```bash
docker network ls | grep exercicio
```

### Passo 5: Teste a comunicação entre containers

```bash
# Entre no container 'api'
docker-compose exec api sh
```

Dentro do container `api`:

```sh
# Consegue acessar o web (mesma rede frontend)
wget -O- http://web:80 2>/dev/null | head -5

# Consegue acessar o database (mesma rede backend)
ping -c 2 database

# NÃO consegue acessar algo fora das redes
ping google.com   # Não funciona sem configurar DNS

exit
```

### Passo 6: Veja os volumes

```bash
docker volume ls | grep exercicio
```

### Passo 7: Pare e remova (sem perder dados)

```bash
docker-compose down
```

**Volume ainda existe!**

```bash
docker volume ls | grep exercicio
# db_data ainda está lá!
```

### Passo 8: Suba novamente (dados mantidos)

```bash
docker-compose up -d
```

Os dados do MySQL **não foram perdidos**!

### Passo 9: Limpe TUDO (incluindo volumes)

```bash
docker-compose down -v
```

Agora sim, tudo foi removido.

---

## ✅ Checklist

- [ ] Criou 3 containers com um comando
- [ ] Acessou http://localhost:8080
- [ ] Entendeu a diferença entre redes `frontend` e `backend`
- [ ] Testou comunicação entre containers
- [ ] Verificou que `depends_on` define ordem de start
- [ ] Viu que volumes persistem após `docker-compose down`
- [ ] Usou `docker-compose down -v` para limpar volumes

---

## 🤔 Questões para Reflexão

1. Por que o `database` está na rede `backend` e não na `frontend`?
2. O que acontece se você remover `depends_on` do serviço `web`?
3. Por que precisamos de `-v` no `docker-compose down` para limpar tudo?

---

## 🎯 Desafio

Adicione um quarto serviço chamado `cache` usando a imagem `redis:alpine`:

```yaml
  cache:
    image: redis:alpine
    container_name: senac_cache
    networks:
      - backend
```

```bash
# Depois de modificar:
docker-compose down
docker-compose up -d

# Verifique que tem 4 containers:
docker-compose ps

# Teste a conexão:
docker-compose exec api ping -c 2 cache
```

---

## 📚 Comandos Novos

| Comando | O que faz |
|---------|-----------|
| `docker network ls` | Lista redes |
| `docker volume ls` | Lista volumes |
| `docker-compose down -v` | Remove containers E volumes |
| `docker-compose exec service cmd` | Executa em serviço específico |

---

## 📊 Diagrama das Redes

```
                      Internet
                         |
                    (8080:80)
                         |
                      ┌────┐
                      │ WEB│ ← Frontend Network
                      └────┘
                         |
                      ┌────┐
                      │API │ ← Frontend + Backend
                      └────┘
                         |
                      ┌────┐
                      │ DB │ ← Backend Network
                      └────┘
```

---

## ➡️ Próximo Exercício

Quando terminar, vá para: `../exercicio-03/`
