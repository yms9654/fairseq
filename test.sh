# DATA=data-bin/ai_hub_sp.ko-en
# CKPT=checkpoints/koen_sp2/checkpoint_best.pt
DATA=data-bin/ai_hub_tok.ko-en
CKPT=checkpoints/koen_tok/checkpoint_best.pt

fairseq-generate $DATA \
    --path $CKPT \
    --batch-size 128 --beam 5 \
    # --remove-bpe

# fairseq-interactive \
#     --path checkpoints/koen/checkpoint_best.pt checkpoints/koen \
#     --beam 5 --source-lang ko --target-lang en