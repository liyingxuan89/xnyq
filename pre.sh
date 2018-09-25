#/bin/bash

#cat yjhb.csv.in |awk '{print $1,$2,$3,$5,$6}' > yjhb.csv.in.1
cat yqlb.csv.in |awk -vOFS='\t' '{print $1,$2,$3,$4,$15}' |sort -n -k 1 -k 2 > yqlb.csv.in.1
