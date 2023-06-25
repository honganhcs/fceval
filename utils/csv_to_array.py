import csv


def ctoa(fp):
    result = []
    f = open(fp)
    reader = csv.reader(f)
    for row in reader:
        if any(row):
            result.append(row)
    return result
