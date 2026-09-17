class RegistroMaterias:

    def __init__(self):
        self.historial_notas = dict()

    def agregar_nota(self, materia:str, tipo:str, nota:float):
        nuevoRegistro = (tipo, nota)
        if materia in self.historial_notas:
            self.historial_notas[materia].append(nuevoRegistro)
        else:
            self.historial_notas[materia] = [nuevoRegistro]

    def promedio_materia(self, materia:str) -> float:
        lista_de_notas = self.historial_notas.get(materia)
        if lista_de_notas is None:
            return 0.0
        suma_total = 0.0
        for tipo_evaluacion, calificacion in lista_de_notas:
            suma_total += calificacion
        cantidad_de_notas = len(lista_de_notas)
        return suma_total / cantidad_de_notas


# Crea tu clase aquí...

# Prueba:
registro = RegistroMaterias()

# Agregamos notas de distintas materias usando tuplas internas
registro.agregar_nota("Fisica", "Examen 1", 14.5)
registro.agregar_nota("Fisica", "Laboratorio", 18.0)
registro.agregar_nota("Estructura de Datos", "Proyecto", 20.0)

# Verificamos la estructura anidada (Diccionario -> Lista -> Tupla)
print("Estructura completa:", registro.historial_notas)
# ESPERADO: {'Fisica': [('Examen 1', 14.5), ('Laboratorio', 18.0)], 'Estructura de Datos': [('Proyecto', 20.0)]}

# Calculamos promedios
print("Promedio Física:", registro.promedio_materia("Fisica"))
# ESPERADO: 16.25 (la suma de 14.5 + 18.0 dividida para 2)

print("Promedio Calculo (No existe):", registro.promedio_materia("Calculo"))
# ESPERADO: 0.0
