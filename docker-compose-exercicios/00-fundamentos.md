# 🐳 Docker Compose - Do Zero ao Avançado

## 📚 Índice

1. [Fundamentos](#fundamentos)
2. [Conceitos Básicos](#conceitos-básicos)
3. [Estrutura do Arquivo](#estrutura-do-arquivo)
4. [Comandos Essenciais](#comandos-essenciais)
5. [Exercícios](#exercícios)

---

## 🎯 Fundamentos

### O que é Docker Compose?

O **Docker Compose** é uma ferramenta para definir e executar múltiplos containers Docker com um único comando. Ele usa arquivos YAML para configurar os serviços da aplicação.

### Por que usar?

| Sem Docker Compose | Com Docker Compose |
|-------------------|-------------------|
| `docker run ...` (repetido várias vezes) | Um único arquivo YAML |
| Sem documentação do ambiente | Ambiente versionado |
| Difícil de reproduzir | `docker-compose up` |
| Ordem manual de start | Ordem automática |

---

## 🏗️ Estrutura Básica

```yaml
version: '3.8'              # Versão do formato

services:                   # Containeres que serão criados
  nome_servico:
    image: nome/imagem      # Imagem a ser usada
    ports:
      - "80:80"            # Porta host:porta container
    environment:            # Variáveis de ambiente
      - VARIAVEL=valor
    volumes:                # Volumes mapeados
      - /host:/container
    networks:               # Redes
      - minha_rede

networks:                   # Definição de redes
  minha_rede:

volumes:                    # Definição de volumes
  meu_volume:
```

---

## 📋 Anatomia de um Serviço

```yaml
web:                          # ← Nome do serviço
  image: nginx:latest         # ← Imagem obrigatória
  container_name: meu_web     # ← Nome do container (opcional)
  restart: always             # ← Política de restart
  ports:
    - "8080:80"               # host:container
    - "443:443"
  environment:                # Ou usando dict:
    NODE_ENV: production
    DB_HOST: mysql
  volumes:
    - ./html:/usr/share/nginx/html    # ← Montagem bind mount
    - dados:/app/dados                # ← Named volume
  depends_on:                 # ← Ordem de start
    - database
  networks:
    - frontend
    - backend
  build:                      # ← Build ao invés de image
    context: ./app
    dockerfile: Dockerfile
```

---

## 🔧 Comandos Essenciais

| Comando | Descrição |
|---------|-----------|
| `docker-compose up` | Cria e inicia containers |
| `docker-compose up -d` | Modo detached (background) |
| `docker-compose down` | Para e remove containers |
| `docker-compose ps` | Lista containers |
| `docker-compose logs` | Mostra logs |
| `docker-compose logs -f` | Logs em tempo real |
| `docker-compose exec service bash` | Executa comando no container |
| `docker-compose exec service nome_comando` | Executa comando |
| `docker-compose stop` | Para containers (mantém) |
| `docker-compose start` | Inicia containers parados |
| `docker-compose restart` | Reinicia containers |
| `docker-compose pull` | Atualiza imagens |
| `docker-compose config` | Valida o YAML |

---

## 🎓 Exercícios Práticos

### Exercício 1: Hello World
Veja: `exercicio-01/`

### Exercício 2: Multi-container
Veja: `exercicio-02/`

### Exercício 3: Volumes e Rede
Veja: `exercicio-03/`

### Exercício 4: Variáveis de Ambiente
Veja: `exercicio-04/`

### Exercício 5: Build Customizado
Veja: `exercicio-05/`

---

## 💡 Dicas Importantes

1. **Indentação matters** - Use espaços, não tabs (YAML)
2. **Portas:** `"host:container"` - host acessa de fora
3. **depends_on** não garante que o serviço está pronto, apenas start
4. **Networks:** Services se comunicam pelo nome do serviço
5. **Volumes persistentes:** Use `docker-compose down -v` para limpar

---

## 📖 Próximos Passos

Após concluir os exercícios, aprenda:
- Docker Compose com múltiplos arquivos (`docker-compose -f`)
- Healthchecks
- Secrets e configs
- Deploy em produção (swarm)
