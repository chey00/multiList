# Aufgabe 1:
# Erstellen Sie eine Funktion addBookToShelf mit dem
# Parameter shelf.
#
# Die Funktion fügt ein neues Buch in ein Fach des
# Bücherregals ein. Dazu fragt es dem Anwender nach der
# Reihe und der Lücke sowie dem Buchtitel.



shelf = list()

# Create a bookshelf with 10 rows and 30 books per row.
for i in range(10):
    row = list()

    for j in range(30):
        row.append(None)

    shelf.append(row)

# Access the shelf:
print(shelf)

# Access the 3rd row
print(shelf[2])

# Access the 4th book in 3rd row
print(shelf[2][3])

# Set book samples
shelf[2][3] = "Rich dad poor dad"
shelf[3][1] = "Eigene KI-Anwendungen programmieren"
shelf[4][4] = "Gregs Tagebuch (Teil 3)"
shelf[1][4] = "Mathematische Formeln und Definitionen"

print(shelf)
