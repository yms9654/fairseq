TEXT=data/ai_hub

fairseq-preprocess --source-lang ko --target-lang en \
    --trainpref $TEXT/train --validpref $TEXT/valid --testpref $TEXT/test \
    --destdir data-bin/ai_hub.ko-en