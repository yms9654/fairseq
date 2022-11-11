DATA=data-bin/sh
# DATA=data-bin/ai_hub_sp
CKPT=checkpoints/koen_transformer_sh_5e-4/checkpoint_best.pt

fairseq-interactive $DATA \
    --path $CKPT \
    --beam 5 \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model --sacrebleu