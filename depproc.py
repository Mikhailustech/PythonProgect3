# Persents real on deposit

def percents(x, y):
     """What percentage of x is y"""
     one_percent = x / 100
     result = y / one_percent
     return result



def print_percents(x,y):
     """Print What percentage of x is y"""
     print("deposit = " +  str(x) + " in this moment " + str(y) + " result in procent " + str(percents(x, y)))
    

print_percents(78,108)
