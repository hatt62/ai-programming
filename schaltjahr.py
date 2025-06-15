def ist_schaltjahr(jahr):
    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        return True
    else:
        return False