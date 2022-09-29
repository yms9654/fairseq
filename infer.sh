DATA=data-bin/ai_hub_sp.ko-en
CKPT=checkpoints/koen_sp/checkpoint_best.pt

fairseq-interactive --path $CKPT data-bin/ai_hub_sp.ko-en \
    --beam 5 --source-lang ko --target-lang en \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model