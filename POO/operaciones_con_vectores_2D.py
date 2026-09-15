class Vector2D:
    history = []
    def __init__(self, x:int , y:int):
        self.x = x
        self.y = y
        tupla = (x,y)
        Vector2D.history.append(tupla)

    def __str__(self) -> str:
        return f"<Vector: x={self.x}, y={self.y}>"

    def __add__(self, other):
        xAxis =  self.x + other.y
        yAxis = self.y + other.y
        return Vector2D(xAxis, yAxis)

class NamedVector (Vector2D):
    def __init__(self, x:int , y:int, name:str):
        super().__init__(x,y)
        self.name = name

    def __str__(self) -> str:
        return f"[Vector {self.name}] x = {self.x} y = {self.y}"
# Tus clases aquí...

# Prueba de escritorio:
v1 = Vector2D(2, 4)
v2 = Vector2D(10, -1)
v3 = NamedVector( 5, 5, "Velocidad")

# Probando __str__
print(v1) # Debe imprimir: <Vector: x=2, y=4>
print(v3) # Debe imprimir: [Vector Velocidad] x=5, y=5

# Probando __add__
v_suma = v1 + v2
print(v_suma) # Debe imprimir: <Vector: x=12, y=3>

# Probando el Atributo de Clase estático
print("Historial de vectores creados:", Vector2D.history)
# Debe imprimir: [(2, 4), (10, -1), (5, 5), (12, 3)]