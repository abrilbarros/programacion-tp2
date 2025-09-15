# Ejercicio 5

# Clase que modela un círculo con radio (en centimetros)
class Circulo:
    # Atributo de clase (constante matematica)
    PI = 3.141592653589793
    
    def __init__(self, radio):
        self.radio = radio # float o int (cm)
        
    # Comando (setter)
    def establecer_radio(self, radio):
        self.radio = radio
    
    # Consultas (getters)
    def obtener_radio(self):
        return self.radio
    
    def obtener_diametro(self):
        return self.radio * 2
    
    def obtener_area(self):
        return Circulo.PI * (self.radio ** 2)
    
    def obtener_perimetro(self):
        return 2 * Circulo.PI * self.radio