print("Ex 1")
b = int(input("Introduceti dimensiunea bazei triunghiului: "))
h = int(input("Introduceti dimensiunea inaltimii triunghiului: "))
aria = int((b*h)/2)
print(type(aria))
print(aria)
print()

print("Ex 2")
parola = 7710
nr = int(input("Introdu parola: "))
if nr==parola:
    print("True - ai ghicit parola")
else:
    print("False - mai incearca")
print()

print("Ex 3")
a = int(input("Introdu primul nr: "))
c = int(input("Introdu al doilea nr: "))
media_aritmetica = float((a+c)/2)
impartire = int(a/c)
putere = int(a**c)
print(f"Media numerelor este {media_aritmetica}\nImpartirea numerelor este {impartire}\nA la puterea b este {putere}")
print()

print("Ex 4")
venit = int(input("Introdu venitul: "))
necesitati = float((50 * venit)/100)
recreere = float((30 * venit)/100)
datorii = float((20 * venit)/100)
print(f"Venit: {venit}\nNecesitati: {necesitati}\nRecreere: {recreere}\nDatorii: {datorii}")