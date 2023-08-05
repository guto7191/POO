from typing import Type
from Interrupitor import Interrupitor

class Pessoa:

    def acender_luz(self, interrupitor: Type[Interrupitor]):
        interrupitor.acender()

    def apagar_luz(self, interrupitor: Type[Interrupitor]):
        interrupitor.apagar()
    
    def dormir():
        print("Dormindo!")
