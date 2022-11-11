DATA=data-bin/sh
# DATA=data-bin/ai_hub_sp
CKPT=checkpoints/koen_transformer_sh_5e-4/checkpoint_best.pt
# CKPT=checkpoints/koen_transformer_1006/checkpoint_best.pt

fairseq-generate $DATA \
    --path $CKPT \
    --batch-size 512 --beam 5 \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model --sacrebleu \
    --gen-subset test