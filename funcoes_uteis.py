from dataclasses import dataclass


@dataclass
class Funcoes:

    def gerar_ir(self, id):
        id += 1
        return id
