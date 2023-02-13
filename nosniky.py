import numpy



class nosnik:
    def __init__(self, typ, l, E, J, F = 0, q = 0, Q = 0, M = 0, Ma = 0, Mb = 0, a = 0, b = 0, c = 0, FrA = 0, FrB = 0, MoMax = 0, alphaA = 0, yMax = 0, alphamax = 0, alphaB = 0, alphaC = 0, yB = 0, yC = 0, alpha = 0, alphaF = 0, y1 = 0, y2 = 0, yF = 0, yDF = 0, alphaAM = 0, alphaBM = 0):
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
                self.yMax =        round((self.F*self.l**3)/(3*self.E*self.J), 4)
                self.yB =          round(self.yMax, 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nyMax = {self.yMax}mm\nyB = {self.alphaB}mm")
            case 2:
                self.FrA =       round(numpy.absolute(self.F), 4)
                self.MoMax =     round((self.F*self.l)/2, 4)
                self.alphaA =    round(0, 4)
                self.alphamax =  round((self.F*self.l**2)/(8*self.E*self.J), 4)
                self.alphaB =    round(self.alphamax, 4)
                self.alphaC =    round(self.alphamax, 4)
                self.yMax =      round((5*self.F*self.l**3)/(48*self.E*self.J), 4)
                self.yC =        round((self.F*self.l**3)/(24*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nalphaC = {self.alphaC}rad\nyMax = {self.yMax}mm\nyC = {self.yC}")
            case 3:
                if self.q == 0:
                    self.q = self.Q/self.l
                self.FrA =       round(numpy.absolute(self.q*self.l), 4)
                self.MoMax =     round((self.q*self.l**2)/2, 4)
                self.alphaA =    round(0, 4)
                self.alphamax =  round((self.q*self.l**3)/(6*self.E*self.J), 4)
                self.alphaB =    round(self.alphamax, 4)
                self.yMax =      round((self.q*self.l**4)/(8*self.E*self.J), 4)
                self.yB =        round(self.alphamax, 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nalphaB = {self.alphaB}rad\nyMax = {self.yMax}mm\nyB = {self.yB}")
            case 4:
                self.FrA =      round(0, 4)
                self.MoMax =    round(self.M, 4)
                self.alphaA =   round(0, 4)
                self.alphamax = round((self.M*self.l)/(self.E*self.J), 4)
                self.yMax =     round((self.M*self.l**2)/(2*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaMax = {self.alphamax}rad\nyMax = {self.yMax}mm")
            case 5:
                if self.q == 0:
                    self.q = self.Q/self.l
                self.FrA =    round((1/2)*(self.q*self.l), 4)
                self.MoMax =  round((self.q*self.l**2)/6, 4)
                self.alphaA = round((self.q*self.l**3)/(24*self.E*self.J), 4)
                self.yMax =   round((self.q*self.l**4)/(30*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nyMax = {self.yMax}mm")
            case 6:
                self.FrA =     round(numpy.absolute(self.F/2), 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round((self.F*self.l)/4, 4)
                self.alphaA =  round((self.F*self.l**2)/(16*self.E*self.J), 4)
                self.alphaB =  round(self.alphaA, 4)
                self.yMax =    round((self.F*self.l**3)/(48*self.E*self.J), 4)
                self.yC =      round(self.yMax, 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyC = {self.yC}mm\nyMax = {self.yMax}mm")
            case 7:
                self.FrA =     round(numpy.absolute((self.F*self.b)/self.l), 4)
                self.FrB =     round(numpy.absolute((self.F*self.a)/self.l), 4)
                self.MoMax =   round((self.F*self.a*self.b)/self.l, 4)
                self.alphaA =  round(((self.F*self.l**2)/(6*self.E*self.J))*((self.b/self.l)-((self.b**3)/(self.l**3))), 4)
                self.alphaB =  round(((self.F*self.l**2)/(6*self.E*self.J))*((2*self.b/self.l)+((self.b**3)/(self.l**3))-((3*self.b**3)/(self.l**2))), 4)
                self.yMax =    round((self.F*self.a**2*self.b**2)/(3*self.E*self.J*self.l), 4)
                self.yC =      round(self.yMax, 4)
                self.yDF =     round(((self.F*self.a*self.c)/(6*self.E*self.J*self.l)*(self.b*(self.b+2*self.a)-self.c**2)), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyC = {self.yC}mm\nyDF = {self.yDF}mm\nyMax = {self.yMax}mm")
            case 8:
                self.FrA =     round(-(self.F*self.a)/self.l, 4)
                self.FrB =     round(-(self.F*(self.a + self.l))/self.l, 4) 
                self.MoMax =   round(self.F*self.a, 4)
                self.alphaF =  round(((self.F*self.a)*(2*self.l+3*self.a))/(6*self.E*self.J), 4)
                self.alphaA =  round((self.F*self.l*self.a)/(3*self.E*self.J), 4)
                self.alphaB =  round(self.alphaB, 4)
                self.yF =      round((self.F*self.a**2)*(self.l+self.a)/(3*self.E*self.J), 4)
                self.yMax =    round((self.F*self.a*self.l**2)/(15.59*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nalphaF = {self.alphaF}rad\nyF = {self.yF}mm\nyMax = {self.yMax}mm")
            case 9:
                self.FrA =     round(self.F, 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round(self.F*self.a, 4)
                self.yMax =    round(((self.F*self.l**3)/(8*self.E*self.J))*(self.a/self.l)*(1-((4*self.a**2)/(3*self.l**2))), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nyMax = {self.yMax}mm")
            case 10:
                self.FrA =     round(self.F, 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round(self.F*self.a, 4)
                self.yMax =    round(((self.F*self.l**3)/(2*self.E*self.J))*(self.a**2/self.l**2)*(1+((2*self.a)/(3*self.l))), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nyMax = {self.yMax}mm")
            case 11:
                if self.q == 0:
                    self.q = self.Q/self.l
                self.FrA =     round(numpy.absolute((self.q*self.l)/2), 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round((self.q*self.l**2)/8, 4)
                self.alphaA =  round((self.q*self.l**3)/(24*self.E*self.J), 4)
                self.alphaB =  round(self.alphaA, 4)
                self.yC =      round((5*self.q*self.l**4)/(384*self.E*self.J), 4)
                self.yMax =    round(self.yC, 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyC = {self.yC}mm\nyMax = {self.yMax}mm")
            case 12:
                self.FrA =     round((self.q*self.l)/6, 4)
                self.FrB =     round(self.FrA*2, 4)
                self.MoMax =   round((self.q*self.l**2)/15.6, 4)
                self.alphaA =  round((7*self.q*self.l**3)/(360*self.E*self.J), 4)
                self.alphaB =  round((8*self.q*self.l**3)/(360*self.E*self.J), 4)
                self.yMax =    round((self.q*self.l**4)/(153*self.E*self.J), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nyMax = {self.yMax}mm")
            case 13:
                self.FrA =     round(self.q*(self.a+self.l/2), 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round(self.q*((self.a**2/2)+(self.l**2/2)), 4)
                self.y1 =      round(((self.q*self.l**4)/(16*self.E*self.J))*((5/24)-(self.a**2/self.l**2)), 4)
                self.y2 =      round(((self.q*self.l**3*self.a)/(24*self.E*self.J))*(((3*self.a**2)/(self.l**3))+((6*self.a**2)/(self.l**2))-1), 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\ny1 = {self.y1}mm\ny2 = {self.y2}mm")
            case 14:
                self.FrA =     round(numpy.absolute(self.Ma/self.l), 4)
                self.FrB =     round(self.FrA, 4)
                self.MoMax =   round(self.Ma, 4)
                self.alphaA =  round((self.Ma*self.l)/(3*self.E*self.J), 4)
                self.alphaB =  round(self.alphaA/2, 4)
                self.alphaAM = round(((2*self.Ma+self.Mb)*self.l)/(6*self.E*self.J), 4)
                self.alphaBM = round(((2*self.Mb+self.Ma)*self.l)/(6*self.E*self.J), 4)
                self.yMax =    round(0.0642*(self.Ma*self.l**2)/(self.E*self.J), 4)
                self.xyMax =   round(0.422*self.l, 4)
                output = (f"FrA = {self.FrA}N\nFrB = {self.FrB}N\nMoMax = {self.MoMax}Nmm\nalphaA = {self.alphaA}rad\nalphaB = {self.alphaB}rad\nalphaAM = {self.alphaAM}rad\nalphaBM = {self.alphaBM}rad\nyMax = {self.yMax}mm\nxyMax = {self.xyMax}mm")
        return output

#nos = nosnik(1, 2000, 450, 100000000, F=5000)
#print(nos.vypocet())