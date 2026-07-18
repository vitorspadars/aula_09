from utils_log import log_decorator



@log_decorator
def soma (x,y):
    return x + y


soma(2,5)
soma(4,6)
soma(4,"3")