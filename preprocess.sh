NAME=test
TEXT=data/$NAME
OUTPUT=data-bin/$NAME

rm -rf $OUTPUT

fairseq-preprocess --source-lang ko --target-lang en \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir $OUTPUT \
    --workers 20 \
    --srcdict data-bin/ai_hub_sp/dict.ko.txt --tgtdict data-bin/ai_hub_sp/dict.en.txt 