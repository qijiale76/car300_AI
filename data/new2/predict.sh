#!/bin/bash
for i in $(seq 1 10)
do
awk 'BEGIN{srand()} {print rand()"\t"$0}' ../neg_25000.txt | sort -nk 1 | head -n 36000 | awk -F "\t" '{print $2}'  > neg_24000.txt
cat neg_24000.txt ../pos_1200.txt > exam.txt
../../../../fastText/fasttext predict ../model3.bin exam.txt >result.txt
head -36000 result.txt > head.txt
tt=`grep __label__1 head.txt |wc -l`
fn=$tt
echo $fn
#tmp=`expr 1182+ $fn`
#rec=`expr 1182 / $tmp `
#echo "recal=" $rec
rm neg_24000.txt exam.txt result.txt head.txt
done
