from konlpy.tag import Kkma, Okt
# from nltk.tokenize import word_tokenize
import sentencepiece as spm

input = "data/ai_hub/train.en"
output = "data/ai_hub_sp/train.en"

# tokenizer = Okt()
sp = spm.SentencePieceProcessor()
sp.Load('data/sp/subword_tokenizer_en.model')
output_fp = open(output, "w")

with open(input) as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        # tok = tokenizer.morphs(line)
        # tok = ' '.join(tok)
        # output_fp.write(tok)
        tok = sp.encode(line, out_type=str)
        tok = ' '.join(tok)
        output_fp.write(tok+'\n')
        print(idx)

output_fp.close()