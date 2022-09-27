OUTPUT=checkpoints/koen_sp2
DATE=20220927_2
DATA=data-bin/ai_hub_sp.ko-en

mkdir -p $OUTPUT
CUDA_VISIBLE_DEVICES=0 fairseq-train $DATA \
    --optimizer nag --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
    --arch transformer_tiny --save-dir $OUTPUT --batch-size 256 \
    --tensorboard-logdir log/tfboard --log-file log/$DATE.log \
    --max-epoch 40