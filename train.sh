OUTPUT=checkpoints/koen

mkdir -p $OUTPUT
CUDA_VISIBLE_DEVICES=0 fairseq-train data-bin/ai_hub.ko-en \
    --optimizer nag --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-tokens 4000 \
    --arch transformer_tiny --save-dir $OUTPUT --batch-size 256 \
    --tensorboard-logdir log/tfboard --log-file log/20220923.log