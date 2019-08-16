python2 data_pre.py ../data/neg_ceshi_0626length_morethan_25000.csv ../data/neg_25000.txt

cp  ../data/neg_25000.txt ../data/neg_25000_bak.txt

file='../data/neg_25000_bak.txt'

sort -n $file | uniq

sort -n $file | awk '{if($0!=line)print; line=$0}'

sort -n $file | sed '$!N; /^\(.*\)\n\1$/!P; D'
