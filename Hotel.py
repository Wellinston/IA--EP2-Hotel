import numpy as np
from Hotel_Satisfacoes import Restricao, SatisfacaoRestricoes

# Restrições
class RestricaoTurnoVazio(Restricao):
  def __init__(self, funcionario1):
    super().__init__([funcionario1])
    self.funcionario1 = funcionario1

  def esta_satisfeita(self, atribuicao):
    if self.funcionario1 not in atribuicao:
      return True
    return atribuicao[self.funcionario1]

class RestricaoTurnoConsecutivo(Restricao):
  def __init__(self, funcionario1, funcionario2):
    super().__init__([funcionario1, funcionario2])
    self.funcionario1 = funcionario1
    self.funcionario2 = funcionario2

  def esta_satisfeita(self, atribuicao):
    if self.funcionario1 not in atribuicao or self.funcionario2 not in atribuicao:
      return True
    return atribuicao[self.funcionario1] != atribuicao[self.funcionario2]

class RestricaoNaoPodeNesseTurno(Restricao):
  def __init__(self, funcionario1, funcionario2):
    super().__init__([funcionario1, funcionario2])
    print(funcionario1)
    self.funcionario1 = funcionario1
    self.funcionario2 = funcionario2

  def esta_satisfeita(self, atribuicao):
    if self.funcionario1 not in atribuicao or self.funcionario2 not in atribuicao:
      return True
    return atribuicao[self.funcionario1] != atribuicao[self.funcionario2]


# Variáveis
habilidades = [
  "Recepção", "Limpeza de Quartos", "Cozinha", "Serviço de Quarto", "Bar",
  "Lavanderia", "Manutenção"
]
diasSemana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]

variaveis = np.array([])

# Formatando todas variaveis
for dia in diasSemana:
  for habilidade in habilidades:
    for i in range(1, 4):
      variaveis = np.append(variaveis, dia + str(i) + "_" + habilidade)

# Setando todos domínios
dominios = {}

pessoas = {
  "João": {"Recepção", "Limpeza de Quartos"},
  "Maria": {"Cozinha", "Serviço de Quarto", "Bar"},
  "Ana": {"Recepção", "Lavanderia"},
  "Carlos": {"Limpeza de Quartos", "Manutenção"},
  "Bruno": {"Cozinha", "Serviço de Quarto"},
  "Paula": {"Recepção", "Limpeza de Quartos", "Bar"},
  "Pedro": {"Manutenção", "Limpeza de Quartos"},
  "Luiza": {"Lavanderia", "Limpeza de Quartos"},
  "Thiago": {"Cozinha", "Bar"},
  "Fernanda": {"Recepção", "Lavanderia", "Serviço de Quarto"},
  "Rafael": {"Cozinha", "Serviço de Quarto", "Bar"},
  "Juliana": {"Recepção", "Limpeza de Quartos"},
  "Caio": {"Manutenção", "Limpeza de Quartos"},
  "Beatriz": {"Manutenção", "Limpeza de Quartos"},
  "Lucas": {"Manutenção", "Limpeza de Quartos", "Bar"},
  "Bruna": {"Cozinha", "Serviço de Quarto"},
  "Marcelo": {"Recepção", "Limpeza de Quartos", "Lavanderia"},
  "Vanessa": {"Cozinha", "Bar"},
  "Danilo": {"Manutenção", "Limpeza de Quartos"},
  "Renata": {"Recepção", "Serviço de Quarto", "Bar"}
}

for variavel in variaveis:
  #Substituir os 20 números pelos nomes das 20 pessoas
  dominios[variavel] = np.array(["João", "Maria", "Ana", "Carlos", "Bruno", "Paula", "Pedro", "Luiza", "Thiago", "Fernanda", "Rafael", "Juliana", "Caio", "Beatriz", "Lucas", "Bruna", "Marcelo", "Vanessa", "Danilo", "Renata"]) 

problema = SatisfacaoRestricoes(variaveis, dominios)
# problema.adicionar_restricao(RestricaoTurnoVazio("seg1_Recepção"))

i = 1
for dia in diasSemana:
  for habilidade in habilidades:
    problema.adicionar_restricao(RestricaoTurnoConsecutivo(dia + str(i) + "_" + habilidade, dia + str(i + 2) + "_" + habilidade))
    
# problema.adicionar_restricao(RestricaoNaoPodeNesseTurno("seg1_Recepção", "seg1_Limpeza de Quartos"))



resposta = problema.busca_backtracking()
if resposta is None:
  print("Nenhuma resposta encontrada")
else:
  print(resposta)

