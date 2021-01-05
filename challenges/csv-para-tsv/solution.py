import csv

with open('dados.csv') as csvin, open('dados.tsv', 'a') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter ='\t')

    for row in csvin:
        tsvout.writerow(row)