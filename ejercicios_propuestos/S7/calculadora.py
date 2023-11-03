from PyQt5.QtCore import pyqtSignal, QObject


class Calculadora(QObject):

    senal_calcular = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.senal_calcular.connect(self.validar_input)
        self.senal_mostrar_resultado = None

    def suma(self, valor1, valor2):
        string_resultado = str(int(valor1) + int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def resta(self, valor1, valor2):
        string_resultado = str(int(valor1) - int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def cuociente(self, valor1, valor2):
        string_resultado = str(float(valor1) / float(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def multiplicacion(self, valor1, valor2):
        string_resultado = str(int(valor1) * int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def validar_input(self, accion):
        # método que recibe como señal un diccionario de la forma
        # accion = {'operación': operacion, 'valor1': valor1, 'valor2: valor2'}
        if self.senal_calcular:
            if accion['valor1'].isnumeric() and accion['valor2'].isnumeric():
                if accion['operacion'] == "sumar":
                    self.suma(accion['valor1'], accion['valor2'])
                elif accion['operacion'] == "restar":
                    self.resta(accion['valor1'], accion['valor2'])
                elif accion['operacion'] == "multiplicar":
                    self.multiplicacion(accion['valor1'], accion['valor2'])
                elif accion['operacion'] == "dividir":
                    self.cuociente(accion['valor1'], accion['valor2'])
            else:
                self.senal_mostrar_resultado.emit('Error: Input inválido')