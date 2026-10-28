# 📝 Exercício 4: Variáveis de Ambiente

## 🎯 Objetivo

Aprender a usar **variáveis de ambiente** para configurar containers Docker.

---

## 📋 Conceitos Novos

### O que são variáveis de ambiente?

São valores passados para o container que controlam comportamento da aplicação **sem alterar código**.

### Sintaxes possíveis:

```yaml
environment:
  # Forma 1: lista (simples)
  - VARIAVEL=valor

  # Forma 2: dicionário (melhor para YAML)
  VARIAVEL: valor

  # Forma 3: múltiplas linhas
  - VAR1=valor1
  - VAR2=valor2
```

### Variáveis do host → Container:

```yaml
# Passa variável do seu computador para o container
MEU_VAR: ${NOME_VAR_HOST}

# Com valor padrão (se não existir no host)
MEU_VAR: ${NOME_VAR_HOST:-valor_padrao}
```

---

## 🏗️ Arquivo Explicado

```yaml
environment:
  # Direto no YAML
  APP_NAME: "Senac Docker App"

  # Referência a variável do host
  MY_HOST_VAR: ${MEU_NOME:-Visitante}
  #           ↑          ↑           ↑
  #        valor    var host    valor padrão

# Porta também pode usar variável
ports:
  - "${APP_PORT:-8080}:5000"
```

---

## 🚀 Passo a Passo

### Passo 1: Entre no diretório

```bash
cd docker-compose-exercicios/exercicio-04/
```

### Passo 2: Suba com valores padrão

```bash
docker-compose up -d
```

### Passo 3: Acesse a aplicação

Abra: http://localhost:8080

Veja as variáveis carregadas!

### Passo 4: Crie um arquivo .env

```bash
cp .env.example .env
```

### Passo 5: Personalize o .env

```bash
nano .env
# Mude MEU_NOME para seu nome
# Mude WORKER para um nome diferente
```

### Passo 6: Suba novamente com novas variáveis

```bash
docker-compose down
docker-compose up -d
```

### Passo 7: Acesse novamente

Abra: http://localhost:8080

As variáveis mudaram!

### Passo 8: Verifique as variáveis no container

```bash
# Ver variáveis do serviço app
docker-compose exec app env | sort

# Ver variáveis do serviço worker
docker-compose exec worker env | sort
```

### Passo 9: Sobrescreva variável na linha de comando

```bash
# Sobrescreve APP_PORT
docker-compose down
APP_PORT=9090 docker-compose up -d

# Acesse: http://localhost:9090
```

---

## ✅ Checklist

- [ ] Entendeu sintaxe de `environment`
- [ ] Criou e usou arquivo `.env`
- [ ] Viu variáveis mudando sem alterar código
- [ ] Usou `${VAR:-padrao}` para valores padrão
- [ ] Sobrescreveu variável na linha de comando

---

## 🤔 Questões para Reflexão

1. Por que usar `.env` ao invés de valores fixos no YAML?
2. Quando usar `${VAR}` e quando usar `${VAR:-padrao}`?
3. O que acontece se a variável do host não existe e não há padrão?

---

## 🎯 Desafios

### Desafio 1: Arquivo .env por ambiente

Crie arquivos para diferentes ambientes:

```bash
# Desenvolvimento
cp .env.example .env.dev
# Edite com valores de dev

# Produção
cp .env.example .env.prod
# Edite com valores de prod

# Use cada um:
docker-compose --env-file .env.dev up -d
docker-compose --env-file .env.prod up -d
```

### Desafio 2: Multiplas variáveis de produção

No `docker-compose.yml`, adicione:

```yaml
  app:
    environment:
      - APP_NAME=${APP_NAME}
      - APP_PORT=${APP_PORT}
      - DB_HOST=${DB_HOST}
      - DB_USER=${DB_USER}
      - DB_PASS=${DB_PASS}
      - REDIS_HOST=${REDIS_HOST}
```

Crie `.env.production`:

```
APP_NAME=Produção App
APP_PORT=80
DB_HOST=db.prod.local
DB_USER=prod_user
DB_PASS=senha_super_secreta
REDIS_HOST=redis.prod.local
```

```bash
docker-compose --env-file .env.production config
# Mostra como ficaria o YAML final
```

---

## 📚 Comandos Novos

| Comando | O que faz |
|---------|-----------|
| `docker-compose exec service env` | Lista variáveis do container |
| `VAR=val docker-compose up` | Sobrescreve variável |
| `--env-file arquivo` | Usa arquivo .env específico |
| `docker-compose config` | Mostra YAML final com variáveis resolvidas |

---

## 🔒 Segurança

⚠️ **NUNCA** commit arquivo `.env` com senhas!

```gitignore
# .gitignore
.env
.env.local
.env.*.local
```

Use apenas `.env.example` com valores de exemplo:

```
# .env.example (OK no git)
DB_PASSWORD=senha_aqui

# .env (NUNCA no git)
DB_PASSWORD=minha_senha_real
```

---

## ➡️ Próximo Exercício

Quando terminar, vá para: `../exercicio-05/`
