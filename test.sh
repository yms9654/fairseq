# fairseq-generate data-bin/iwslt14.tokenized.de-en \
#     --path checkpoints/fconv/checkpoint_best.pt \
#     --batch-size 128 --beam 5

fairseq-interactive --path checkpoints/koen/checkpoint_best.pt