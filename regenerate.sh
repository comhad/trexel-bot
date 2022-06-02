echo Regenerating in 5, press Ctrl+C to cancel
sleep 5
echo -e \\n\\n\\n\\n\\n > vocab.csv
rm lines.txt
touch lines.txt
echo Cleared files, regenerating...
for FILE in `find transcripts/*`;
do python3 sentence_extraction.py $FILE && python3 split_scripts.py $FILE;
done
echo Regeneration complete!