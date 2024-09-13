import networkx as nx
import matplotlib.pyplot as plt
import sys


with open("grafo.txt", 'rb') as f:
  g: nx.DiGraph = nx.read_weighted_edgelist(f, create_using=nx.DiGraph)


def calculaTempoCedo(g: nx.DiGraph, no):
  """ Calcula o tempo mais cedo olhando os predecessores do nó."""
  tempos = []
  for p in g.predecessors(no):
    tempos.append(calculaTempoCedo(g, p) + g.get_edge_data(p, no)['weight'])
  
  # Retorna o maior dos valores em tempo, ou 0, se estiver vazio.
  # Tempo estará vazio se o nó for o inicial
  return max(tempos, default=0.0)

def calculaTempoTarde(g: nx.DiGraph, no):
  tempos = []
  for s in g.successors(no):
      tempos.append(calculaTempoCedo(g, s) - g.get_edge_data(no, s)['weight'])
  
  # Retorna o menor dos valores em tempo, ou o tempo mínimo do nó, se estiver vazio.
  # Tempo estará vazio se o nó for o final
  return min(tempos, default=calculaTempoCedo(g, no))

def calculaCaminhoCritico(g: nx.DiGraph):
  # Descobre nó inicial
  for n in g:
    if len(list(g.predecessors(n))) == 0:
        no = n

  caminho = [no]
  
  while no != None:
    suc = list(g.successors(no))
    for s in suc:
      # Caso algum sucessor tiver tempo mínimo e máximo iguais, selecionamos ele
      if calculaTempoCedo(g, s) == calculaTempoTarde(g, s):
          # adicionamos ele no caminho
          caminho.append(s)
          # agora vamos olhar os sucessores desse nó
          no = s
      # se não houverem sucessores, quer dizer que encontramos o nó final
    if len(suc) == 0:
      no = None
    
  
  return caminho

temp_min = {}
for n in g:
   # aqui, salvamos o tempo cedo do nó `n` no dicionário temp_min
   temp_min[n] = calculaTempoCedo(g, n)

temp_max = {}
for n in g:
   # aqui, salvamos o tempo terde do nó `n` no dicionário temp_max
   temp_max[n] = calculaTempoTarde(g, n)
print("Tempos mais cedo:", temp_min)
print("Tempos mais tarde:", temp_max)
print("Caminho crítico:", calculaCaminhoCritico(g))

