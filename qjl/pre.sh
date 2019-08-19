python2 data_pre.py ../data/neg_ceshi_0626length_morethan_25000.csv ../data/neg_25000.txt

cp  ../data/neg_25000.txt ../data/neg_25000_bak.txt

file='../data/neg_25000_bak.txt'

sort -n $file | uniq >../data/neg_25000_bak_1.txt

sort -n ../data/neg_25000_bak.txt | awk '{if($0!=line)print; line=$0}'  > ../data/neg_25000_bak_2.txt

sort -n ../data/neg_25000_bak_2.txt | sed '$!N; /^\(.*\)\n\1$/!P; D' > ../data/neg_25000_bak_3.txt

python3 data_pre_json.py  ../data/data_all.json  ../data/data_pos.txt  ../data/data_neg.txt

awk 'BEGIN{srand()} {print rand()"\t"$0}' ../data/neg_25000.txt | sort -nk 1 | head -n 9200 | awk -F "\t" '{print $2}'  > neg_9200.txt

awk 'BEGIN{srand()} {print rand()"\t"$0}' ../data/data_pos.txt | sort -nk 1 | head -n 9200 | awk -F "\t" '{print $2}'  > pos_9200.txt

head -8000 ../data/neg_9200.txt >neg_8000.txt
head -8000 ../data/pos_9200.txt >pos_8000.txt
cat neg_8000.txt pos_8000.txt > train.txt
tail -1200 ../data/neg_9200.txt >neg_1200.txt
tail -1200 ../data/pos_9200.txt >pos_1200.txt
cat neg_1200.txt pos_1200.txt > exam.txt

../../../fastText/fasttext supervised -input train.txt -output model
 ../../../fastText/fasttext test model.bin exam.txt


awk 'BEGIN{srand()} {print rand()"\t"$0}' ../data/neg_25000.txt | sort -nk 1 | head -n 80000 | awk -F "\t" '{print $2}'  > neg_80000.txt
cat neg_80000.txt pos_1200.txt > exam.txt

tail -1200 ../data/neg_9200.txt >neg_1200.txt
tail -1200 ../data/pos_9200.txt >pos_1200.txt



 ../../../../fastText/fasttext predict ../model3.bin xlxd_exam.txt >result.txt