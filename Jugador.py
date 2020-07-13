class Jugador():

    def __init__(self, nombre):
        self.dict_grande = {'E1': 1, 'E2': 1, 'E3': 21845, 'E4': 5, 'E5': 21, 'E6': 85, 'E7': 341, 'ES': 1365,
                            'EC': 5461, 'ER': 21845,
                            'B1': 1, 'B2': 1, 'B3': 21845, 'B4': 5, 'B5': 21, 'B6': 85, 'B7': 341, 'BS': 1365,
                            'BC': 5461, 'BR': 21845,
                            'O1': 1, 'O2': 1, 'O3': 21845, 'O4': 5, 'O5': 21, 'O6': 85, 'O7': 341, 'OS': 1365,
                            'OC': 5461, 'OR': 21845,
                            'C1': 1, 'C2': 1, 'C3': 21845, 'C4': 5, 'C5': 21, 'C6': 85, 'C7': 341, 'CS': 1365,
                            'CC': 5461, 'CR': 21845, }

        self.dict_chica = {'ER': 1, 'EC': 5, 'ES': 21, 'E7': 85, 'E6': 341, 'E5': 1365, 'E4': 5461, 'E3': 1,
                           'E2': 21845, 'E1': 21845,
                           'BR': 1, 'BC': 5, 'BS': 21, 'B7': 85, 'B6': 341, 'B5': 1365, 'B4': 5461, 'B3': 1,
                           'B2': 21845, 'B1': 21845,
                           'OR': 1, 'OC': 5, 'OS': 21, 'O7': 85, 'O6': 341, 'O5': 1365, 'O4': 5461, 'O3': 1,
                           'O2': 21845, 'O1': 21845,
                           'CR': 1, 'CC': 5, 'CS': 21, 'C7': 85, 'C6': 341, 'C5': 1365, 'C4': 5461, 'C3': 1,
                           'C2': 21845, 'C1': 21845}

        self.dict_par = {'E1': 1, 'E2': 1, 'E3': 10, 'E4': 4, 'E5': 5, 'E6': 6, 'E7': 7, 'ES': 8, 'EC': 9, 'ER': 10,
                         'B1': 1, 'B2': 1, 'B3': 10, 'B4': 4, 'B5': 5, 'B6': 6, 'B7': 7, 'BS': 8, 'BC': 9, 'BR': 10,
                         'O1': 1, 'O2': 1, 'O3': 10, 'O4': 4, 'O5': 5, 'O6': 6, 'O7': 7, 'OS': 8, 'OC': 9, 'OR': 10,
                         'C1': 1, 'C2': 1, 'C3': 10, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'CS': 8, 'CC': 9, 'CR': 10}

        self.dict_juego = {'E1': 1, 'E2': 1, 'E3': 10, 'E4': 4, 'E5': 5, 'E6': 6, 'E7': 7, 'ES': 10, 'EC': 10, 'ER': 10,
                           'B1': 1, 'B2': 1, 'B3': 10, 'B4': 4, 'B5': 5, 'B6': 6, 'B7': 7, 'BS': 10, 'BC': 10, 'BR': 10,
                           'O1': 1, 'O2': 1, 'O3': 10, 'O4': 4, 'O5': 5, 'O6': 6, 'O7': 7, 'OS': 10, 'OC': 10, 'OR': 10,
                           'C1': 1, 'C2': 1, 'C3': 10, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'CS': 10, 'CC': 10, 'CR': 10}
        self.nombre = nombre

    def dar_mano(self, cartas):
        self.cartas = cartas
        self.grande = 0
        self.chica = 0
        self.par = 0
        self.juego = 0

    def puntuacion_baraja(self):
        self.pareja = False
        self.segunda_pareja = False
        self.trio = False
        self.duples = False
        self.temp_cartas = [] + self.cartas
        for x in self.cartas:
            self.grande += self.dict_grande[x]
            self.chica += self.dict_chica[x]
            self.juego += self.dict_juego[x]


            try:
                self.temp_cartas.remove(x)
            except:
                pass
            self.borrar = []
            for y in self.temp_cartas:
                if self.dict_par[y] == self.dict_par[x]:
                    self.borrar.append(y)

                    if self.segunda_pareja:
                        self.temp_carta2 = self.dict_par[y]
                        self.duples = True
                        self.pareja = False

                    if not self.pareja and not self.segunda_pareja:
                        self.pareja = True
                        self.temp_carta = self.dict_par[y]


                    elif not self.trio and not self.segunda_pareja:
                        self.trio = True
                        self.pareja = False

            if self.pareja:
                self.segunda_pareja = True

            for y in self.borrar:
                self.temp_cartas.remove(y)

        if self.pareja and not self.duples:
            self.par = self.temp_carta
        elif self.trio:
            self.par = self.temp_carta * 10 + 1
        elif self.duples:
            if self.temp_carta2 > self.temp_carta:
                self.par = self.temp_carta2 * 100 + self.temp_carta + 1
            else:
                self.par = self.temp_carta * 100 + self.temp_carta2 + 1

        if self.juego == 31:
            self.juego = 310
        elif self.juego == 32:
            self.juego = 41

    def bonus_mano(self, bonus):
        self.grande += bonus
        self.chica += bonus
        self.par += bonus
        self.juego += bonus  # recordar

    def par_y_juego(self):
        self.puntuacion_baraja()
        if self.juego > 30 and self.par > 0:
            return True
        else:
            return False