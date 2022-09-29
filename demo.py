import gradio as gr
from fairseq.models.transformer import TransformerModel

ko2en = TransformerModel.from_pretrained(
    'checkpoints/koen_transformer_full',
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path='data-bin/ai_hub_sp.ko-en',
    bpe='sentencepiece',
    sentencepiece_model='data/sp/subword_tokenizer_ko.model'
)

def translate(input):    
    return ko2en.translate(input)

demo = gr.Interface(fn=translate, inputs="text", outputs="text")

demo.launch()   