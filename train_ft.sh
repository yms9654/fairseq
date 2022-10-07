OUTPUT=checkpoints/koen_transformer_teracomix_1006
DATE=20221006
DATA=data-bin/teracomix-1006

mkdir -p $OUTPUT

# CUDA_VISIBLE_DEVICES=0 fairseq-train $DATA \
#     --optimizer nag --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
#     --arch transformer --save-dir $OUTPUT --batch-size 1024 \
#     --tensorboard-logdir log/tfboard --log-file log/$DATE.log \
#     --max-epoch 40

CUDA_VISIBLE_DEVICES=0 fairseq-train $DATA \
    --arch transformer --share-decoder-input-output-embed \
    --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
    --lr 5e-4 --lr-scheduler inverse_sqrt --warmup-updates 4000 \
    --dropout 0.3 --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --max-tokens 4096 \
    --save-dir $OUTPUT \
    --tensorboard-logdir log/tfboard/$DATE --log-file log/$DATE.log \
    --batch-size 1024 --max-epoch 40 --amp \
    --finetune-from-model checkpoints/koen_transformer_full/checkpoint_best.pt 