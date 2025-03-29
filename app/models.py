from datetime import datetime
from dataclasses import dataclass

@dataclass
class Transacao():
    valor: float
    dataHora: datetime

    def getdataHora(self):
        return self.dataHora

    def getValor(self):
        return self.valor


