def ist_schaltjahr(jahr):
    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        return True
    else:
        return False
    
# Eingaberoutine erstellt
jahr = int(input("Gib ein Jahr ein: "))
if ist_schaltjahr(jahr):
    print(f"{jahr} ist ein Schaltjahr.")
else:
    print(f"{jahr} ist kein Schaltjahr.")