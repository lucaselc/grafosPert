# Análise de Grafo PERT

Este projeto contém um programa para calcular os tempos mais cedo, tempos mais tarde e o caminho crítico em um grafo PERT. O grafo é representado por um conjunto de atividades com duração específica, e o programa utiliza este grafo para determinar o cronograma do projeto.

## Descrição do Problema

O objetivo é calcular:

- **Tempos Mais Cedo**: O tempo mais cedo em que cada atividade pode começar sem atrasar o projeto.
- **Tempos Mais Tarde**: O tempo mais tarde em que cada atividade pode começar sem atrasar o projeto.
- **Caminho Crítico**: O caminho mais longo através do grafo, que determina a duração total do projeto.

## Arquivos

- **pert.py**: O código Python que realiza o cálculo dos tempos mais cedo, tempos mais tarde e o caminho crítico.
- **grafo.txt**: Arquivo de entrada contendo as atividades do grafo, no formato:


## Executando o Programa

1. **Instale o Python** (Python 3.x recomendado) se ainda não estiver instalado.

2. **Instale as dependências** necessárias usando pip:
 ```bash
 pip install networkx
