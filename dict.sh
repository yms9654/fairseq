TEXT=data/teracomix
OUTPUT=data-bin/dict

fairseq-preprocess --source-lang ko --target-lang en \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir $OUTPUT \
    --workers 20 --dict-only