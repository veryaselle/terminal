import csv

with open("/work/users/ao582fpoy/train/track_artist1.csv", 'r') as csvin, \
        open("C:/Users/verya/Desktop/DS23/BigData/tsv_track_artist1.tsv", 'w', newline='') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)

with open("/work/users/ao582fpoy/train/tsv_track_artist1.tsv", 'r', encoding='utf-8') as tbd:
    print(tbd.read())

# 10651
