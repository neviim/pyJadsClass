# Somando dois vetores.
#
# Neviim - 2018

class ObjString(object):
    """ Serve para representar um objeto como uma string
    """
    def __init__(self):
        self.valor1 =  1
        self.valor2 = "2"

    def __repr__(self):
        return str(self.valor1) + ", " + self.valor2



if __name__ == '__main__':

    x = {'a': 1, 'b': 2}
    y = {'b': 3, 'c': 4}

    z = {**x, **y}

    print(z)
    print( )

    # Class ObjString

    obj = ObjString()
    print(obj)

