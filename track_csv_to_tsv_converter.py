import csv

with open("/work/users/ao582fpoy/train/track.csv", 'r') as csvin, \
        open("/work/users/ao582fpoy/train/tsv_track.tsv", 'w', newline='') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)

with open("/work/users/ao582fpoy/train/tsv_track.tsv", 'r', encoding='utf-8') as tbd:
    print(tbd.read())

# 288