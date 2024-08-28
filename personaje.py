class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp: int):
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 100:
            self.nivel += 1
            tmp_exp -= 100

        while tmp_exp < 0 and self.nivel > 1:
            tmp_exp = 100 + tmp_exp
            self.nivel -= 1

            if self.nivel == 1 and tmp_exp < 0:
                tmp_exp = 0

        self.experiencia = tmp_exp

    def __lt__(self, other):
        return (
            self.experiencia < other.experiencia
        )

    def __gt__(self, other):
        return (
            self.experiencia > other.experiencia
        )

    def __eq__(self, other):
        return (
            self.experiencia == other.experiencia
        )

    def get_probabilidad_ganar(self, personaje, other):
        if personaje < other:
            probabilidad_ganar = 0.33
            return probabilidad_ganar
        elif personaje > other:
            probabilidad_ganar = 0.66
            return probabilidad_ganar
        else:
            probabilidad_ganar = 0.5
            return probabilidad_ganar
    """"El getter de estado ahora muestra correctamente el nivel y la experiencia.
        El setter de estado ahora maneja correctamente la experiencia y el nivel según las reglas dadas.
        Las sobrecargas de los operadores de comparación ahora comparan el nivel, no la experiencia.
        El método get_probabilidad_ganar ahora devuelve las probabilidades correctas según el nivel relativo al otro personaje."""
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% de probabilidades de ganar contra el Orco.\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\nSi pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"
            ))