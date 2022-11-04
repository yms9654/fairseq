DATA=data-bin/test
# DATA=data-bin/ai_hub_sp
CKPT=checkpoints/koen_transformer_test/checkpoint_last.pt

fairseq-generate $DATA \
    --path $CKPT \
    --batch-size 512 --beam 5 \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model --sacrebleu