from app.models import Transacao
from typing import List


class TransacaoRepository():
    def __init__(self):
        self.transacoes: List[Transacao] = []


    def addTransacao(self, Transacao):
        self.transacoes.append(Transacao)

    def limpar(self):
        self.transacoes.clear()


    def getTransacao(self):
        return self.transacoes.copy()