from typing import Any, Optional
from dataclasses import dataclass
from percepcoes import PercepcoesJogador
from agentes.Desenhador import Desenhador_mundo

class ProblemaSemSolucaoException(Exception):
    pass


@dataclass
class No():
    estado: Any
    acao: Optional[Any] = None
    pai: Optional['No'] = None

    def calcular_profundidade(self):
        raiz = not self.pai
        return 0 if raiz else self.pai.calcular_profundidade() + 1
    
    def caminho_acoes(self) -> list:
        """Retorna uma lista com as ações em ordem para atingir o estado
        que este nó armazena.
        """
        raiz = not self.pai
        return [] if raiz else self.pai.caminho_acoes() + [self.acao]

    @classmethod
    def criar_no_filho(cls, problema, pai, acao):
        novo_estado = problema.resultado(pai.estado, acao)
        '''custo_solucao = pai.custo_solucao + problema.custo(pai.estado, acao, novo_estado)'''
        return cls(novo_estado, acao, pai)
    
    def __repr__(self) -> str:
        return f'No({self.estado!r},{self.acao!r})'

solucao = []
def busca_em_arvoreBFS(self, problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial(self))]
    while borda:
        folha = borda.pop(0)
        if problema.teste_objetivo(folha.estado):
            return folha
        for acao in problema.acoes(folha.estado):
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)
            Desenhador_mundo.DesenharMundo(self, expandido.estado)
    raise ProblemaSemSolucaoException()

def busca_em_arvoreDFS(self, problema) -> No:
    """ Retorna uma solucao ou falha"""
    borda = [No(problema.estado_inicial(self))]
    while borda:
        folha = borda.pop()
        if problema.teste_objetivo(folha.estado):
            return folha
        for acao in problema.acoes(folha.estado):
            expandido = No.criar_no_filho(problema, folha, acao)
            borda.append(expandido)
            Desenhador_mundo.DesenharMundo(self, expandido.estado)
    raise ProblemaSemSolucaoException()

busca_arvore_bfs = busca_em_arvoreBFS
busca_arvore_dfs = busca_em_arvoreDFS
