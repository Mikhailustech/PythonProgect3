# Application for determining interest income on investments

def percents(x, y):
     """What percentage of x is y"""
     one_percent = x / 100
     result = (y / one_percent) - 100
     return result


def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))


def difine_color(result):
     """Difine color for the result in percents"""
     if result < 0:
          color = out_red(result)
     elif result > 0:
          color = out_yellow(result)
     else:
          color = out_blue(result)
     return color


def print_percents(x,y):
     """Print What percentage of x is y"""
     print("deposit = " +  str(x) + " in this moment " + str(y) + " result in procents " + ""),(str(difine_color(percents(x, y))))


# Set the current values and see the result in the required color
print_percents(79.11,119.54)
