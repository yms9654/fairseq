from cProfile import label
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

callback = gr.CSVLogger()

with gr.Blocks() as demo:
    input = gr.Textbox(label="Input")
    output = gr.Textbox(label="Output")
    input.submit(fn=translate, inputs=input, outputs=output)
    
    btn = gr.Button('오류보고')
    callback.setup([input, output], 'flagged')
    btn.click(lambda *args: callback.flag(args), [input, output], None, preprocess=False)
demo.launch(share=True)   