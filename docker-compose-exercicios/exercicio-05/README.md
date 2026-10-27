# 📝 Exercício 5: Build Customizado

## 🎯 Objetivo

Aprender a **construir imagens customizadas** com Docker Compose usando Dockerfile.

---

## 📋 Conceitos Novos

### `build` ao invés de `image`

```yaml
# Usando imagem pronta
services:
  app:
    image: python:3.12

# Build customizado
services:
  app:
    build:
      context: .          # Diretório com os arquivos
      dockerfile: Dockerfile  # Nome do Dockerfile
```

### Quando usar build?

- Sua aplicação precisa de dependências específicas
- Quer customizar a imagem base
- Precisa incluir arquivos na imagem
- Quer otimizar para produção

---

## 🏗️ Arquivos Explicados

### Dockerfile

```dockerfile
FROM python:3.12-slim        # Imagem base
WORKDIR /app                # Diretório de trabalho
RUN pip install flask pymysql   # Instala dependências
COPY app.py .                # Copia código
EXPOSE 5000                  # Expõe porta
CMD ["python", "app.py"]    # Comando padrão
```

### docker-compose.yml

```yaml
services:
  app:
    build:                   # Constrói imagem
      context: .             # Contexto do build
      dockerfile: Dockerfile
    volumes:
      - ./app.py:/app/app.py   # Monta código (dev mode)
```

---

## 🚀 Passo a Passo

### Passo 1: Entre no diretório

```bash
cd docker-compose-exercicios/exercicio-05/
```

### Passo 2: Veja os arquivos

```bash
ls -la
# Temos: Dockerfile, docker-compose.yml, app.py, init.sql, requirements.txt
```

### Passo 3: Suba os containers

```bash
docker-compose up -d
```

Primeiro vez vai **buildar** a imagem (demora mais):

```
Creating network "exercicio-05_default"
Creating volume "exercicio-05_db_data"
Building app...
[+] Building 10.5s ...
 => => naming to senac_custom_app
Creating senac_custom_db...
Creating senac_custom_app...
```

### Passo 4: Veja a imagem criada

```bash
docker images | grep senac
```

Você verá a imagem `exercicio-05-app`

### Passo 5: Acesse a aplicação

Abra: http://localhost:8080

Você verá os dados do banco!

### Passo 6: Edite o código (hot reload)

```bash
nano app.py
# Mude algo, salve, e atualize o navegador
# Mudanças aparecem instantaneamente!
```

Isso funciona porque montamos só o código com volumes!

### Passo 7: Veja os logs

```bash
docker-compose logs -f app
```

### Passo 8: Teste o health check

```bash
curl http://localhost:8080/health
```

### Passo 9: Rebuild após mudanças no Dockerfile

```bash
# Se mudar o Dockerfile, precisa rebuild:
docker-compose up -d --build
```

### Passo 10: Limpe

```bash
docker-compose down -v
```

Para limpar também a imagem:

```bash
docker rmi exercicio-05-app
```

---

## ✅ Checklist

- [ ] Entendeu `build` vs `image`
- [ ] Criou imagem customizada com Dockerfile
- [ ] Viu imagem criada com `docker images`
- [ ] Testou hot reload do código
- [ ] Usou `--build` para rebuildar
- [ ] Entendeu quando usar volumes em desenvolvimento

---

## 🤔 Questões para Reflexão

1. Por que montamos só `app.py` com volume e não tudo?
2. Quando você deve rebuildar a imagem?
3. Qual a diferença entre `COPY` no Dockerfile e `volumes` no compose?

---

## 🎯 Desafios

### Desafio 1: Multi-stage build

Crie um Dockerfile otimizado:

```dockerfile
# Build stage
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app.py .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

```bash
docker-compose build
docker-compose up -d
```

### Desafio 2: Args no build

No `docker-compose.yml`:

```yaml
  app:
    build:
      context: .
      args:
        VERSION: "1.0"
        ENV: production
```

No `Dockerfile`:

```dockerfile
ARG VERSION=1.0
ARG ENV=development
ENV APP_VERSION=${VERSION}
ENV APP_ENV=${ENV}
```

---

## 📚 Comandos Novos

| Comando | O que faz |
|---------|-----------|
| `docker-compose build` | Builda as imagens |
| `docker-compose up --build` | Builda e sobe containers |
| `docker-compose build service` | Builda só um serviço |
| `docker images | grep nome` | Vê imagens criadas |
| `docker rmi nome_imagem` | Remove imagem |

---

## 🔄 Ciclo de Desenvolvimento

```
┌─────────────────────────────────────────────────────────────┐
│                     DESENVOLVIMENTO                         │
├─────────────────────────────────────────────────────────────┤
│  1. Edita código                                           │
│  2. Salva                                                  │
│  3. Atualiza navegador (hot reload via volume)            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              MUDOU DEPENDÊNCIAS OU DOCKERFILE               │
├─────────────────────────────────────────────────────────────┤
│  docker-compose up -d --build                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Comparação: image vs build

| | Imagem Pronta | Build Customizado |
|---|--------------|-------------------|
| **Sintaxe** | `image: nome:tag` | `build: ./dir` |
| **Velocidade** | Instantâneo | Demora no primeiro uso |
| **Custo** | Nada | CPU no build |
| **Controle** | Limitado | Total |
| **Uso** | Serviços genéricos | Aplicação própria |
| **Exemplo** | `mysql`, `nginx`, `redis` | Seu app Python |

---

## 🎓 Parabéns!

Você completou todos os 5 exercícios de Docker Compose!

### O que você aprendeu:

1. ✅ Subir container simples
2. ✅ Múltiplos containers e redes
3. ✅ Volumes e persistência
4. ✅ Variáveis de ambiente
5. ✅ Build customizado

### Próximos passos:

- Healthchecks
- Docker Swarm
- Kubernetes
- CI/CD com Docker

---

## 📖 Referência Rápida

```yaml
# Modelo completo
version: '3.8'
services:
  nome:
    image: nome:tag              # ou build: .
    build: .                     # Constrói imagem
    container_name: nome         # Nome do container
    restart: always              # Política de restart
    ports:
      - "host:container"
    environment:
      VAR: valor
    volumes:
      - host:container
    depends_on:
      - outro_servico
    networks:
      - minha_rede
volumes:
  vol_name:
networks:
  rede_name:
```
