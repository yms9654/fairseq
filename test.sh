DATA=data-bin/ai_hub_sp.ko-en
CKPT=checkpoints/koen_transformer/checkpoint_best.pt
# DATA=data-bin/ai_hub_tok.ko-en
# CKPT=checkpoints/koen_tok/checkpoint_best.pt

fairseq-generate $DATA \
    --path $CKPT \
    --batch-size 512 --beam 5 \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model --sacrebleu