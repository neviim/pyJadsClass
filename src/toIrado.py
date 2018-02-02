
# Polinomio da paz.
#
# Neviim - 2018

class ToIrado:
    def __init__(self, *problema):
        self.problema = problema
        
    def __repr__(self):
        return 'Paz(*{!r})'.format(self.problema)
    
    def __add__(self, other):
        return ToIrado(*(x + y for x, y in zip(self.problema, other.problema)))



if __name__ == '__main__':
    paz1 = ToIrado(1, 2, 3)     #  x² + 2x + 3
    paz2 = ToIrado(3, 2, 1)     # 3x² + 4x + 3

    print(paz1)
    print(paz2)
    print(paz1 + paz2)
