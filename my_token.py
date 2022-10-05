import sentencepiece as spm

input = "data/teracomix/full.en"
output = "data/teracomix/clean_sp.en"
model = 'data/sp/subword_tokenizer_en.model'

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