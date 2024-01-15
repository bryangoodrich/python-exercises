import csv
from collections import namedtuple

def read_csv(source, columns, header=True):
    csv_row = namedtuple('CSVRow', columns)
    data = []
    with open(source, encoding="UTF-8") as fh:
        reader = csv.reader(fh)
        if header:
            next(reader)
        
        for row in reader:
            datum = csv_row(*row)  
            data.append(datum)
    
    return data


if __name__ == "__main__":
    columns = ['name', 'mfr', 'type', 'calories', 'protein', 'fat', 
        'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 
        'shelf', 'weight', 'cups', 'rating']
    cereals = read_csv("data/cereal.csv", columns)
    
    topline = ("Calories", "Cereal")
    print(f"{topline[0]:>10} {topline[1]}")
    for cereal in cereals:
        print(f"{cereal.calories:>10} {cereal.name}")
    #   Calories Cereal
    #     70 100% Bran
    #    120 100% Natural Bran
    #     70 All-Bran
    #     50 All-Bran with Extra Fiber
    #    110 Almond Delight
    #    110 Apple Cinnamon Cheerios
    #    110 Apple Jacks
    #    130 Basic 4
    #     90 Bran Chex
    #     90 Bran Flakes
    #    120 Cap'n'Crunch
    #    110 Cheerios
    #    120 Cinnamon Toast Crunch
