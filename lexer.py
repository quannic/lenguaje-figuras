
# Lexer simple para dividir línea en tokens
def tokenizar(linea):
    tokens = []
    token = ""
    for c in linea:
        if c in "(),":
            if token:
                tokens.append(token.strip())
                token = ""
            tokens.append(c)
        else:
            token += c
    if token:
        tokens.append(token.strip())
    return [t for t in tokens if t != ","]
