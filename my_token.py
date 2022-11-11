import sentencepiece as spm

lang = 'en'
dir = 'sh'
input = f'data/{dir}/full_clean.{lang}'
output = f'data/{dir}/train.{lang}'
model = f'data/sp/subword_tokenizer_{lang}.model'

sp = spm.SentencePieceProcessor()
sp.Load(model)
output_fp = open(output, "w")

with open(input) as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        tok = sp.encode(line, out_type=str)
        tok = ' '.join(tok)
        output_fp.write(tok+'\n')
        print(idx)

output_fp.close()