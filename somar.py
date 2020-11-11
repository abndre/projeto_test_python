def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def delta(a, b, c):
    delta = b*2 - 4*a*c
    return delta

def check_delta(delta):
    if delta >= 0:
        return True
    else:
        return False

def calc_raizes(a, b, c):
    # TODO: Calcular raizes
    pass
    
def baskara(a, b, c):
    delt = delta(a, b, c)
    if check_deta(delt):
        return calc_raizes(a, b, c)
    else:
        return False
