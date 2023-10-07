
Datentyp 	Was ist das? 	Beispiele
int 	Ganzzahlen 	1 -25 0
float 	kommazahlen 	0.5 0.0 1.0 10000000000.4
complex
bool 	Boolean 	True False

NoneType 	Nix 	None

WERTEVORRÄTE
str 	Text 	"eaurtn ", " ", ‘wort’
list 	Listen (flexibel) 	[“hallo”, 1, 2], [], [1], [1, 2, [4, “hallo”]]
tuple 	Tupel (schnell) 	(1, 2, 3), (48.0, 10.0), (0, 71, 255)
dict 	Dictionaries 	{“red”:(1, 0, 0), “green”:(0, 1,0)}, {“alexis”:25, “kim”:12}
set 		{1, 2, 3}
Die Sache mit den =

ein = : Aufforderung
zwei == : Frage
for-Schleifen

for schleifenvariable in wertevorrat:
machlustigesachenmit(schleifenvariable)
+=

a = a + 5
a += 5
“erhöhe a um 5”
if, for und while


wort1 = "   "
wort2 = "hallo"


if wort2 == wort1:  # Vergleiche die Wörter
# if    False      :
    print("Die beiden sind gleich.")
else:
    print("Die beiden sind nicht gleich.")


# for buchstabe in wort2:
#     print(buchstabe*5)

# for i in range(10):
#     print(i*4)

counter = 0

while counter < 10:
    zahl = input("Gib mir eine Zahl: ")
    if counter < -5:
        break
    try:
        counter = counter + int(zahl)
    except ValueError:
        print("Huiuiuiui")
    print(f"counter ist jetzt {counter}")
    #     counter += zahl


