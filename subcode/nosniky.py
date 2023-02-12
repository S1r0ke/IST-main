import numpy



class nosnik:
    def __init__(self, typ, l, E, J, F = 0, q = 0, Q = 0, M = 0, Ma = 0, Mb = 0, a = 0, b = 0, c = 0, FrA = 0, FrB = 0, MoMax = 0, alphaA = 0, yMax = 0, alphamax = 0, alphaB = 0, alphaC = 0, yB = 0, yC = 0, alpha = 0, alphaF = 0, y1 = 0, y2 = 0, yDF = 0, alphaAM = 0, alphaBM = 0):
        self.typ = typ
        self.F = F
        self.l = l
        self.E = E
        self.J = J
        self.q = q
        self.Q = Q
        self.M = M
        self.a = a
        self.b = b
        self.c = c
        self.Ma = Ma
        self.Mb = Mb

    def vypocet(self):
        match self.typ:
            case 1:
                self.FrA =         round(numpy.absolute(self.F), 4)
                self.MoMax =       round(self.F*self.l, 4)
                self.alphaA =      round(0, 4)
                self.alphamax =    round((self.F*self.l**2)/(2*self.E*self.J), 4)
                self.alphaB =      round(self.alphamax, 4)
                self.ymax =        round((self.F*self.l**3)/(3*self.E*self.J), 4)
                self.yB =          round(self.ymax, 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nyMax = {self.ymax}mm\nyB = {self.alphaB}mm")
            case 2:
                self.FrA =       round(numpy.absolute(self.F), 4)
                self.MoMax =     round((self.F*self.l)/2, 4)
                self.alphaA =    round(0, 4)
                self.alphamax =  round((self.F*self.l**2)/(8*self.E*self.J), 4)
                self.alphaB =    round(self.alphamax, 4)
                self.alphaC =    round(self.alphamax, 4)
                self.ymax =      round((5*self.F*self.l**3)/(48*self.E*self.J), 4)
                self.yC =        round((self.F*self.l**3)/(24*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nalphaC = {self.alphaC}rad\nyMax = {self.ymax}mm\nyC = {self.yC}")
            case 3:
                if self.q == 0:
                    self.q = self.Q/self.l
                self.FrA =       round(numpy.absolute(self.q*self.l), 4)
                self.MoMax =     round((self.q*self.l**2)/2, 4)
                self.alphaA =    round(0, 4)
                self.alphamax =  round((self.q*self.l**3)/(6*self.E*self.J), 4)
                self.alphaB =    round(self.alphamax, 4)
                self.ymax =      round((self.q*self.l**4)/(8*self.E*self.J), 4)
                self.yB =        round(self.alphamax, 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nyMax = {self.ymax}mm\nyB = {self.yB}")
            case 4:
                self.FrA =      round(0, 4)
                self.MoMax =    round(self.M, 4)
                self.alphaA =   round(0, 4)
                self.alphamax = round((self.M*self.l)/(self.E*self.J), 4)
                self.ymax =     round((self.M*self.l**2)/(2*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nyMax = {self.ymax}mm")
            case 5:
                if self.q == 0:
                    self.q = self.Q/self.l
                self.FrA =    round((1/2)*(self.q*self.l), 4)
                self.MoMax =  round((self.q*self.l**2)/6, 4)
                self.alphaA = round((self.q*self.l**3)/(24*self.E*self.J), 4)
                self.ymax =   round((self.q*self.l**4)/(30*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nyMax = {self.ymax}mm")
            case 6:
                self.FrA =     round(numpy.absolute(self.F/2), 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round((self.F*self.l)/4, 4)
                self.alphaA =  round((self.F*self.l**2)/(16*self.E*self.J), 4)
                self.alphaB =  round(self.alphaA, 4)
                self.ymax =    round((self.F*self.l**3)/(48*self.E*self.J), 4)
                self.yC =      round(self.ymax, 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyC = {self.yC}mm\nyMax = {self.ymax}mm")
            case 7:
                self.FrA =     round(numpy.absolute((self.F*self.b)/self.l), 4)
                self.FrB =     round(numpy.absolute((self.F*self.a)/self.l), 4)
                self.MoMax =   round((self.F*self.a*self.b)/self.l, 4)
                self.alphaA =  round(((self.F*self.l**2)/(6*self.E*self.J))*((self.b/self.l)-((self.b**3)/(self.l**3))), 4)
                self.alphaB =  round(((self.F*self.l**2)/(6*self.E*self.J))*((2*self.b/self.l)+((self.b**3)/(self.l**3))-((3*self.b**3)/(self.l**2))), 4)
                self.ymax =    round((self.F*self.a**2*self.b**2)/(3*self.E*self.J*self.l), 4)
                self.yC =      round(self.ymax, 4)
                self.yDF =     round(((self.F*self.a*self.c)/(6*self.E*self.J*self.l)*(self.b*(self.b+2*self.a)-self.c**2)), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyC = {self.yC}mm\nyDF = {self.yDF}mm\nyMax = {self.ymax}mm")




        return output

#nos = nosnik(1, 2000, 450, 100000000, F=5000)
#print(nos.vypocet())