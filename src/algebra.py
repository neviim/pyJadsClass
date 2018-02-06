# Algebra vetorial em python.
#
# Neviim - 2018

class Vet():
    """ docstring para Avet
            dado dois vetor(x, y) eles possam ser somados.

                va = Vet(-3, 7)
                vb = Vet( 6, 2)
                soma = va + vb
                print(soma)         
                
                $> Vet(3, 9)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v2):
        return Vet(self.x + v2.x, self.y + v2.y)
    
    def __sub__(self, v2):
        return Vet(self.x - v2.x, self.y - v2.y)

    def __str__(self):
        return 'Vet('+str(self.x)+', '+str(self.y)+')'


def main():
    a = Vet(-3, 7)
    b = Vet( 6, 2)
    S1 =  a + b
    S2 = S1 - a

    print(S1)   # S1 =  a + b
    print(S2)   # b  = S1 - a


if __name__ == '__main__':
    main()