class Developer:
    def escribir_codigo(self):
        return f"Escribiendo codigo en Python"

class Manager:
    def gestionar_equipo(self):
        return f"Gestionando un equipo de 5 personas"

class TechLead(Developer, Manager):
    def __init__(self, nombre:str, _salario:float):
        self.nombre = nombre
        self._salario = _salario
    @property
    def salario (self):
        return self._salario
    @salario.setter
    def salario (self, nuevosalario:float):
        if self._salario > nuevosalario:
            raise ValueError("No se puede reducir el salario")
        else:
            self._salario = nuevosalario

# Crea tus clases aquí...

# Prueba:
lider = TechLead("Dennis", 2000)

# Probando Herencia Múltiple
print(lider.escribir_codigo())     # Esperado: Escribiendo código en Python
print(lider.gestionar_equipo())    # Esperado: Gestionando un equipo de 5 personas

# Probando Encapsulamiento (Getter)
print(f"Salario inicial de {lider.nombre}: ${lider.salario}")

# Probando Encapsulamiento (Setter exitoso)
lider.salario = 2500
print(f"Nuevo salario: ${lider.salario}")

# Probando Encapsulamiento (Setter fallido - debe arrojar ValueError)
# lider.salario = 1500  # Descomenta esta línea para probar que explota

