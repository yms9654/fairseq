TEXT=data/teracomix
OUTPUT=data-bin/teracomix-1005

fairseq-preprocess --source-lang ko --target-lang en \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir $OUTPUT \
    --srcdict data-bin/dict/update.ko.txt --tgtdict data-bin/dict/update.en.txt \
    --workers 20 