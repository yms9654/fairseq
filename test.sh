# fairseq-generate data-bin/ai_hub.ko-en \
#     --path checkpoints/koen/checkpoint_best.pt \
#     --batch-size 128 --beam 5 --cpu

fairseq-interactive \
    --path checkpoints/koen/checkpoint_best.pt \
    --cpu --beam 5 --source-lang ko --target-lang en \