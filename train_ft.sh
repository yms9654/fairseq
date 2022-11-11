OUTPUT=checkpoints/koen_transformer_sh
DATE=20221109
DATA=data-bin/sh

mkdir -p $OUTPUT

CUDA_VISIBLE_DEVICES=0 fairseq-train $DATA \
    --arch transformer --share-decoder-input-output-embed \
    --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 \
    --lr 5e-5 --lr-scheduler inverse_sqrt --warmup-updates 4000 \
    --dropout 0.3 --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --max-tokens 4096 \
    --save-dir $OUTPUT \
    --tensorboard-logdir log/tfboard/$DATE --log-file log/$DATE.log \
    --batch-size 1024 --max-epoch 100 --amp \
    --finetune-from-model checkpoints/koen_transformer_1006/checkpoint_best.pt 