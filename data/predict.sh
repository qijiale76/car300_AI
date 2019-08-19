awk 'BEGIN{srand()} {print rand()"\t"$0}' ../neg_25000.txt | sort -nk 1 | head -n 24000 | awk -F "\t" '{print $2}'  > neg_24000.txt

cat neg_24000.txt ../pos_1200.txt > exam.txt

../../../../fastText/fasttext predict../ model.bin exam.txt >result.txt

head -24000 result4.txt > head.txt

$fn=grep __label__1 head.txt |wc -l

$rec=expr(1182/(1182+$fn))
echo "recal=" $fn

rm neg_24000.txt exam.txt result.txt head.txt
