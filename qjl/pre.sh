python2 data_pre.py ../data/neg_ceshi_0626length_morethan_25000.csv ../data/neg_25000.txt

cp  ../data/neg_25000.txt ../data/neg_25000_bak.txt

file='../data/neg_25000_bak.txt'

sort -n $file | uniq >../data/neg_25000_bak_1.txt

sort -n ../data/neg_25000_bak.txt | awk '{if($0!=line)print; line=$0}'  > ../data/neg_25000_bak_2.txt

sort -n ../data/neg_25000_bak_2.txt | sed '$!N; /^\(.*\)\n\1$/!P; D' > ../data/neg_25000_bak_3.txt

python3 data_pre_json.py  ../data/data_all.json  ../data/data_pos.txt  ../data/data_neg.txt
