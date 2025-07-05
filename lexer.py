
def tokenizar(linea):
    return linea.replace(",", " ").replace("(", " ").replace(")", " ").split()
