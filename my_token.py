import sentencepiece as spm

input = "data/ai_hub/clean.ko"
output = "data/ai_hub_sp/clean.ko"

sp = spm.SentencePieceProcessor()
sp.Load('data/sp/subword_tokenizer_ko.model')
output_fp = open(output, "w")

with open(input) as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        tok = sp.encode(line, out_type=str)
        tok = ' '.join(tok)
        output_fp.write(tok+'\n')
        print(idx)

output_fp.close()