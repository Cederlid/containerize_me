import csv

def process():
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

if __name__ == '__main__':
    process()
