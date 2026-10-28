

# 📝 Exercício 1: Hello World - Primeiro Container

## 🎯 Objetivo

Subir seu primeiro container usando Docker Compose e entender os comandos básicos.

---

## 📋 Teoria

### O que vamos fazer?

1. Subir um servidor Nginx
2. Acessar via navegador
3. Aprender comandos básicos

### Arquivo docker-compose.yml explicado:

```yaml
version: '3.8'        # Versão do formato do compose

services:             # Lista de containers (serviços)
  web:                # Nome do nosso serviço
    image: nginx:alpine   # Imagem a ser baixada
    container_name: senac_web   # Nome do container
    ports:
      - "8080:80"     # Porta 8080 do host → porta 80 do container
    restart: unless-stopped   # Reinicia se parar, exceto se parado manualmente
```

---

## 🚀 Passo a Passo

### Passo 1: Entre no diretório

```bash
cd docker-compose-exercicios/exercicio-01/
```

### Passo 2: Valide o arquivo

```bash
docker-compose config
```

✅ **Se não aparecer erro, seu YAML está correto!**

### Passo 3: Suba o container

```bash
docker-compose up -d
```

Você verá:
```
Creating network "exercicio-01_default"...
Creating senac_web...
```

### Passo 4: Verifique se está rodando

```bash
docker-compose ps
```

Você deve ver:
```
NAME        COMMAND          SERVICE   STATUS   PORTS
senac_web   "/docker-entry…"   web      Up       0.0.0.0:8080->80/tcp
```

### Passo 5: Acesse no navegador

Abra: http://localhost:8080

Você verá a página **"Welcome to nginx!"**

### Passo 6: Veja os logs

```bash
# Logs do serviço
docker-compose logs web

# Logs em tempo real (Ctrl+C para sair)
docker-compose logs -f web
```

### Passo 7: Entre no container

```bash
docker-compose exec web sh
```

Dentro do container:
```sh
# Você está DENTRO do container agora!
ls -la
cat /etc/os-release
exit
```

### Passo 8: Pare o container

```bash
docker-compose stop
```

### Passo 9: Suba novamente

```bash
docker-compose start
```

### Passo 10: Limpe tudo

```bash
docker-compose down
```

---

## ✅ Checklist

- [ ] Validou o YAML com `docker-compose config`
- [ ] Subiu com `docker-compose up -d`
- [ ] Acessou http://localhost:8080
- [ ] Viu os logs com `docker-compose logs`
- [ ] Entrou no container com `docker-compose exec`
- [ ] Parou com `docker-compose stop`
- [ ] Reiniciou com `docker-compose start`
- [ ] Removeu com `docker-compose down`

---

## 🤔 Questões para Reflexão

1. Por que usamos `"8080:80"` e não só `"80"`?
2. O que acontece se você rodar `docker-compose down` ao invés de `stop`?
3. Qual a diferença entre `restart: always` e `restart: unless-stopped`?

---

## 🎯 Desafio

Modifique o arquivo para:
- Usar a porta `9090` ao invés de `8080`
- Mudar o nome do container para `meu_nginx`

```bash
# Depois de modificar:
docker-compose down
docker-compose up -d
# Acesse: http://localhost:9090
```

---

## 📚 Resumo dos Comandos Aprendidos

| Comando | O que faz |
|---------|-----------|
| `docker-compose config` | Valida o YAML |
| `docker-compose up -d` | Cria e inicia containers |
| `docker-compose ps` | Lista containers |
| `docker-compose logs` | Mostra logs |
| `docker-compose logs -f` | Logs em tempo real |
| `docker-compose exec` | Executa comando no container |
| `docker-compose stop` | Para containers |
| `docker-compose start` | Inicia containers |
| `docker-compose down` | Para e remove containers |

---

## ➡️ Próximo Exercício

Quando terminar, vá para: `../exercicio-02/`
