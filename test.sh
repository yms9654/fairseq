DATA=data-bin/teracomix
# DATA=data-bin/ai_hub_sp.ko-en
# CKPT=checkpoints/koen_transformer_full/checkpoint_best.pt
CKPT=checkpoints/koen_transformer_teracomix/checkpoint_best.pt

fairseq-generate $DATA \
    --path $CKPT \
    --batch-size 512 --beam 5 \
    --bpe sentencepiece \
    --sentencepiece-model data/sp/subword_tokenizer_ko.model --sacrebleu 
    # --replace-unk --dataset-impl=raw