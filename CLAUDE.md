# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of Python programming exercises from Senac 2026, organized by chapter/unit (directories 1-10). Each directory corresponds to a learning module covering different programming concepts.

## Directory Structure

```
senac_2026/
├── 1/        # Aritmética básica e entrada/saída
├── 2/        # Expressões lógicas
├── 3/        # Algoritmos e criação de lógica
├── 4/        # Funções pré-definidas (strings)
├── 5/        # Mais funções pré-definidas
├── 6/        # Estruturas de repetição
├── 7/        # Condicionais
├── 8/        # Listas
├── 9/        # Mais sobre listas
└── 10/       # Exercícios finais/avaliação
```

Each directory contains:
- `n-x.py` — Python solutions to exercises (e.g., `7-1.py`, `7-2.py`)
- `Atividade XX - … .pdf` — Assignment PDF with exercise descriptions
- `ListaXXExercicioX.por` — Portuguese reference files with original problem statements

## Code Conventions

All Python files follow this pattern:

```python
def inicio():
    # entrada de dados
    # processamento
    # saida de dados

if __name__ == "__main__":
    inicio()
```

- Comments are in Portuguese: `# entrada de dados`, `# processamento`, `# saida de dados`
- Main logic is encapsulated in an `inicio()` function
- Standard entry point using `if __name__ == "__main__"`

## Running Exercises

To run any exercise:

```bash
python3 n/n-x.py
```

Example:
```bash
python3 7/7-1.py
```

## Development Notes

- This is a learning repository; code prioritizes clarity over optimization
- Variable names and prompts are in Portuguese to match the learning context
- No build process or dependencies — pure Python with standard library only
- No tests are present — exercises are run manually to verify output
