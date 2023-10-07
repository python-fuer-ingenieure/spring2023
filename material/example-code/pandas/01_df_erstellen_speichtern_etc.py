import pandas as pd
import numpy as np

# aus einem Array:
arr = np.random.randn(6, 4)
df1 = pd.DataFrame(arr, columns=list("ABCD"))

# aus einem Dictionary
dinge = {
    "Gewicht": [10.1, 5.0, 8.3, 7.2],
    "Farbe": ["rot", "grün", "blau", "transparent"],
    "Verfügbarkeit": [False, True, True, False],
    "Preis": 8.99 # alle kosten gleich viel
}
artikelnummern = ["A107", "A108", "A109", "A110"]
df2 = pd.DataFrame(dinge, index=artikelnummern)

# jede Spalten kann eingenen Datentyp haben
print(df2.dtypes)






# als CSV-Datei speichern
df2.to_csv("dinge.csv")


# Datei laden (Python allgemein (unabhängig von Pandas))
fname = "dinge.csv"
with open(fname, "r") as csv_file:
    txt = csv_file.read()
print(txt)


# Pandas-Funktion um Daten in DataFrame zu laden
# (Erkennt Spaltenüberschriften automatisch)
df2_new = pd.read_csv(fname)


from IPython.display import display
display(df2_new)  # Jupyter-Notebook-spezifische Anzeige





# eine Spalte auswählen (-> pd.Series)
df2 ["Preis"]
df2.Preis # äquivalent (wenn möglich)

# eine Zeile über Index-Wert auswählen
df2.loc ["A108"]

# mehrere Zeilen, mehrere Spalten ( -> pd.DataFrame)
df2.loc ["A108":"A109", ["Gewicht","Farbe"]]

# über numerischen Index
df2.iloc [0:2, [0, 3]]

# einzelne Elemente schreiben
df2.loc ["A108","Gewicht"] = 16.4 # neuen Wert zuweisen
df2.loc ["A108","Gewicht"] /= 2 # Wert halbieren

# nachschauen, ob es geklappt hat
df2.iloc [1, 0] # Zeilenindex: 1, Spaltenindex: 0
# mehrere Elemente ver ä ndern

df2.loc ["A108":"A109","Preis"] *= 0.7 # 30% Rabatt




# neue Spalte
df2 ["Laenge"] = [10, 20, 30, 40]
# neue Zeile
df2.loc ["X400"] = [15, "lila", True, 25.00, 50]


# Series - Objekt mit bool - Einträgen erzeugen
tmp_df = df2.Gewicht > 8

# diese bool - Datenreihe zur Indizierung nutzen
df2 [ tmp_df ]

# das ganze in einem Schritt :
df2 [ df2.Gewicht > 8]




df2.describe()

df2.Preis.mean()
df2.Gewicht.median()
df2.Gewicht.max()

# kombinieren mit boolscher Indizierung:
df2 [df2.Gewicht > 8]. Gewicht.mean()
# Funktion auf jede Spalten anwenden
# (Kummulative Summer inhaltlich hier nicht sinnvoll - egal)
df2.apply(np.cumsum )
df2 [["Preis", "Gewicht"]].apply(np.diff)
