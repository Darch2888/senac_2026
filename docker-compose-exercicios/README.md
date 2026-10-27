# 🐳 Docker Compose - Exercícios Práticos

Bem-vindo ao curso prático de **Docker Compose**!

## 📚 Estrutura do Curso

```
docker-compose-exercicios/
├── 00-fundamentos.md      # Teoria completa
├── exercicio-01/           # Hello World
│   ├── docker-compose.yml
│   └── README.md
├── exercicio-02/           # Múltiplos Containers
│   ├── docker-compose.yml
│   └── README.md
├── exercicio-03/           # Volumes
│   ├── docker-compose.yml
│   ├── init.sql
│   ├── html/
│   └── README.md
├── exercicio-04/           # Variáveis de Ambiente
│   ├── docker-compose.yml
│   ├── app.py
│   ├── .env.example
│   └── README.md
└── exercicio-05/           # Build Customizado
    ├── docker-compose.yml
    ├── Dockerfile
    ├── app.py
    ├── init.sql
    ├── requirements.txt
    └── README.md
```

---

## 🎯 Por onde começar?

### 1. Leia a teoria

```bash
cat 00-fundamentos.md
```

### 2. Siga em ordem

Comece pelo **Exercício 1** e avance sequencialmente.

```bash
cd exercicio-01/
cat README.md    # Leia as instruções
```

---

## 📋 Pré-requisitos

- Docker instalado
- Docker Compose instalado
- Conhecimento básico de Linux

### Verificar instalação:

```bash
docker --version
docker-compose --version
```

---

## 🚀 Comandos Úteis

```bash
# Ver containers rodando
docker-compose ps

# Ver logs
docker-compose logs -f

# Parar tudo
docker-compose down

# Parar e limpar volumes
docker-compose down -v

# Ver redes
docker network ls

# Ver volumes
docker volume ls
```

---

## 📊 Roteiro de Estudos

| Exercício | Tema | Tempo Estimado |
|-----------|------|----------------|
| 01 | Hello World | 15 min |
| 02 | Múltiplos Containers | 30 min |
| 03 | Volumes | 30 min |
| 04 | Variáveis de Ambiente | 25 min |
| 05 | Build Customizado | 35 min |
| **Total** | **Curso Completo** | **~2.5 horas** |

---

## 🎓 Certificação

Ao completar todos os exercícios, você saberá:

- [x] Subir containers com Docker Compose
- [x] Trabalhar com múltiplos serviços
- [x] Configurar redes Docker
- [x] Usar volumes para persistência
- [x] Gerenciar variáveis de ambiente
- [x] Construir imagens customizadas
- [x] Desenvolver com hot reload

---

## 💡 Dicas

1. **Leia os READMEs** - Cada exercício tem instruções detalhadas
2. **Execute os comandos** - Aprenda fazendo, não só lendo
3. **Faça os desafios** - Estão no final de cada README
4. **Reflita** - Responda às questões propostas
5. **Experimente** - Modifique os arquivos e teste

---

## 🆘 Problemas Comuns

### Porta já em uso

```bash
# Verifique o que está usando a porta
sudo lsof -i :8080

# Ou mude a porta no docker-compose.yml
ports:
  - "9090:80"   # Usa 9090 ao invés de 8080
```

### Container não inicia

```bash
# Ver os logs
docker-compose logs nome_servico

# Ver o que aconteceu
docker-compose ps -a
```

### Permissões negadas

```bash
# Adicione seu usuário ao grupo docker
sudo usermod -aG docker $USER
newgrp docker
```

---

## 📖 Recursos Adicionais

- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/)
- [Awesome Docker Compose](https://github.com/vegasbrianc/docker-compose)

---

## 👨‍💻 Autor

Material didático para Senac 2026

**Divirta-se aprendendo Docker!** 🐳
