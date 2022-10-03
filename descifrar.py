from operator import itemgetter

frecuencias = [[16.78,'E'],[11.96,'A'],[8.69,'O'],[8.37,'L'],[7.88,'S'],[7.01,'N'],[6.87,'D'],[4.94,'R'],[4.80,'U'],[4.15,'I'],[3.31,'T'],[2.92,'C'],[2.776,'P'],[2.12,'M'],[1.54,'Y'],[1.53,'Q'],[0.92,'B'],[0.89,'H'],[0.73,'G'],[0.52,'F'],[0.39,'V'],[0.30,'J'],[0.29,'Ñ'],[0.15,'Z'],[0.06,'X'],[0.00,'K'],[0.00,'W']];

mACifrar = {
       "a": "l", "b": "f",
       "c": "w", "d": "o",
       "e": "a", "f": "y",
       "g": "u", "h": "i",
       "i": "s", "j": "v",
       "k": "z", "l": "m",
       "m": "n", "n": "x",
       "ñ": "ñ", "o": "p",
       "p": "b", "q": "d",
       "r": "c", "s": "r",
       "t": "j", "u": "t",
       "v": "q", "w": "e",
       "x": "g", "y": "h",
       "z": "k",
       }

CifrarAM = {v: k for k, v in mACifrar.items()}
alfabeto = "qwertyuiopasdfghjklñzxcvbnm"

mensaje = input("introduce  el mensaje a descifrar ")
mensaje = mensaje.lower()
cifrado = ""

for c in mensaje :
    if c not in alfabeto:
        cifrado += c
    else:
        cifrado += CifrarAM[c]

letras = []
longitud = 0
for c in cifrado:
    if c in alfabeto:
        longitud += 1
        if c not in letras:
            letras.append(c)

freqLetra = []
for c in letras:
    freqLetra.append([round(cifrado.count(c) / longitud * 100, 2), c])

freqLetra = sorted(freqLetra, key=itemgetter(0), reverse=True)
textoDescifrado = cifrado

index = 0
for f, c in freqLetra:
    textoDescifrado = textoDescifrado.replace(c, frecuencias[index][1])
    index += 1

print("\n Texto descifrado \n"+textoDescifrado)
