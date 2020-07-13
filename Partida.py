import random
from Jugador import Jugador


class Partida():

    def __init__(self, nombres):
        self.jugadores = []  # 0 y 2  grupo 1, 1 y 3  grupo 2
        for x in nombres:
            self.jugadores.append(Jugador(x))
        self.baraja = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'ES', 'EC', 'ER',
                       'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'BS', 'BC', 'BR',
                       'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'OS', 'OC', 'OR',
                       'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'CS', 'CC', 'CR']

        self.puntos_equipo1 = 0
        self.puntos_equipo2 = 0
        self.mano = 0

    def barajar(self):
        self.mano += 1
        if self.mano == 4:
            self.mano = 0
        self.temp_baraja = self.baraja
        self.cartas_descartadas = []
        for x in self.jugadores:
            mano = []
            for y in range(0, 4):
                carta = random.choice(self.temp_baraja)
                self.temp_baraja.remove(carta)
                mano.append(carta)
            x.dar_mano(mano)

    def mus(self, descartes):  # descartes = [[t,f,f,f],[f,t,t,f],[t,t,t,t],[f,f,f,t]] por ejemplo
        for x in range(0, 3):
            mano = []
            for y in descartes[x]:
                carta_actual = self.jugadores[x].cartas.pop(0)
                if y:
                    if self.temp_baraja == []:
                        self.temp_baraja = self.cartas_descartadas
                        self.cartas_descartadas = []
                    carta = random.choice(self.temp_baraja)
                    self.temp_baraja.remove(carta)
                    self.cartas_descartadas.append(carta_actual)
                else:
                    carta = carta_actual
                mano.append(carta)

            self.jugadores[x].dar_mano(mano)

    def calc_jugadas(self):
        for x in range(0, len(self.jugadores)):
            self.jugadores[x].puntuacion_baraja()
            if x - self.mano < 0:
                self.jugadores[x].bonus_mano(float(-(x - self.mano)) / 10)
            else:
                self.jugadores[x].bonus_mano(0.4 - float(x - self.mano) / 10)

            print self.jugadores[x].cartas
            print self.jugadores[x].juego

    def grande(self, apuesta=0, t1=None, t2=None):
        if t1:
            self.puntos_equipo1 += t1
        elif t2:
            self.puntos_equipo2 += t2
        else:
            self.puntos = 0
            for x in self.jugadores:
                self.puntos = max(x.grande, self.puntos)
            for x in range(0, len(self.jugadores)):
                if self.jugadores[x].grande == self.puntos:
                    if (x + 2) % 2 == 0:
                        self.puntos_equipo1 += apuesta
                    else:
                        self.puntos_equipo2 += apuesta

    def chica(self, apuesta=0, t1=None, t2=None):
        if t1:
            self.puntos_equipo1 += t1
        elif t2:
            self.puntos_equipo2 += t2
        else:
            self.puntos = 0
            for x in self.jugadores:
                self.puntos = max(x.chica, self.puntos)
            for x in range(0, len(self.jugadores)):
                if self.jugadores[x].chica == self.puntos:
                    if (x + 2) % 2 == 0:
                        self.puntos_equipo1 += apuesta
                    else:
                        self.puntos_equipo2 += apuesta

    def par(self, apuesta=0, t1=None, t2=None):
        if t1:
            self.puntos_equipo1 += t1
            for x in range(0, 3, 2):
                if self.jugadores[x].par < 0.5:
                    pass
                elif self.jugadores[x].par < 11:
                    self.puntos_equipo1 += 1
                elif self.jugadores[x].par < 102:
                    self.puntos_equipo1 += 2
                else:
                    self.puntos_equipo1 += 3

        elif t2:
            self.puntos_equipo2 += t2
            for x in range(1, 4, 2):
                if self.jugadores[x].par < 0.5:
                    pass
                elif self.jugadores[x].par < 11:
                    self.puntos_equipo2 += 1
                elif self.jugadores[x].par < 102:
                    self.puntos_equipo2 += 2
                else:
                    self.puntos_equipo2 += 3
        else:
            self.puntos = 0
            for x in self.jugadores:
                self.puntos = max(x.par, self.puntos)
            for x in range(0, len(self.jugadores)):
                if self.jugadores[x].par == self.puntos:
                    if (x + 2) % 2 == 0:
                        self.puntos_equipo1 += apuesta
                        for x in range(0, 3, 2):
                            if self.jugadores[x].par < 0.5:
                                pass
                            elif self.jugadores[x].par < 11:
                                self.puntos_equipo1 += 1
                            elif self.jugadores[x].par < 102:
                                self.puntos_equipo1 += 2
                            else:
                                self.puntos_equipo1 += 3
                    else:
                        self.puntos_equipo2 += apuesta
                        for x in range(1, 4, 2):
                            if self.jugadores[x].par < 0.5:
                                pass
                            elif self.jugadores[x].par < 11:
                                self.puntos_equipo2 += 1
                            elif self.jugadores[x].par < 102:
                                self.puntos_equipo2 += 2
                            else:
                                self.puntos_equipo2 += 3

    def juego(self, apuesta=0, t1=None, t2=None, punto=False):
        if t1:
            self.puntos_equipo1 += t1
            if punto:
                self.puntos_equipo1 += 1
            for x in range(0, 3, 2):
                if self.jugadores[x].juego < 30.6:
                    pass
                elif self.jugadores[x].juego > 310:
                    self.puntos_equipo1 += 3
                else:
                    self.puntos_equipo1 += 2

        elif t2:
            self.puntos_equipo2 += t2
            if punto:
                self.puntos_equipo2 += 1
            for x in range(1, 4, 2):
                if self.jugadores[x].juego < 30.6:
                    pass
                elif self.jugadores[x].juego > 310:
                    self.puntos_equipo2 += 3
                else:
                    self.puntos_equipo2 += 2
        else:
            self.puntos = 0
            for x in self.jugadores:
                self.puntos = max(x.juego, self.puntos)
            for x in range(0, len(self.jugadores)):
                if self.jugadores[x].juego == self.puntos:
                    if (x + 2) % 2 == 0:
                        self.puntos_equipo1 += apuesta
                        if punto:
                            self.puntos_equipo1 += 1
                        for y in range(0, 3, 2):
                            if self.jugadores[y].juego < 30.6:
                                pass
                            elif self.jugadores[y].juego > 310:
                                self.puntos_equipo1 += 3

                            else:
                                self.puntos_equipo1 += 2


                    else:
                        self.puntos_equipo2 += apuesta
                        if punto:
                            self.puntos_equipo2 += 1
                        for y in range(1, 4, 2):
                            if self.jugadores[y].juego < 30.6:
                                pass
                            elif self.jugadores[y].juego > 310:
                                self.puntos_equipo2 += 3
                            else:
                                self.puntos_equipo2 += 2

    def comprobar_final(self):
        if self.puntos_equipo1 >= 40:
            return 1
        elif self.puntos_equipo2 >= 40:
            return 2
        else:
            return None

    def par_y_juego(self,pos):
        return self.jugadores[pos].par_y_juego()

    def es_mano(self,pos):
        self.mano = pos
