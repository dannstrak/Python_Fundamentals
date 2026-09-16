class GamerProfile :
    platform = 'PC'

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
        self.games = {}
    def add_game (self, game_name , hours):
        if game_name in self.games:
            self.games[game_name] += hours
        else:
            self.games[game_name] = hours

    def __gt__(self, other):
        return self.level > other.level

class ProGamer (GamerProfile):
    def __init__(self, username: str, level: int, team:str):
        super().__init__(username, level)
        self.team = team
    def __str__(self) -> str:
        return f'[Team: {self.team}] {self.username} - Nivel: {self.level}'


# Crea tus clases aquí...

# Prueba de escritorio:
jugador1 = GamerProfile("Dennis", 25)

# Simulamos jugar varias sesiones
jugador1.add_game("Forza Horizon 5", 40)
jugador1.add_game("Forza Horizon 5", 10) # Debería sumar y quedar en 50
jugador1.add_game("Brawl Stars", 15)

# Creamos un jugador profesional
jugador2 = ProGamer("Faker", 99, "T1")

# Probando __str__ del ProGamer
print(jugador2)
# ESPERADO: [T1] Faker - Nivel: 99

# Probando el diccionario interno
print(jugador1.games)
# ESPERADO: {'Forza Horizon 5': 50, 'Brawl Stars': 15}

# Probando la sobrecarga del operador >
print("¿Es Faker mayor que Dennis?:", jugador2 > jugador1)
# ESPERADO: True

# Probando la variable de clase estática
print("Plataforma:", ProGamer.platform)
# ESPERADO: PC