import csv

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# 
games = load_csv(r'C:\Users\alexs\OneDrive\Рабочий стол\PractPython\pract3\db.csv')
print(*games[:4],sep='\n')