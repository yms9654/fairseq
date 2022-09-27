# from konlpy.tag import Kkma, Okt
from nltk.tokenize import word_tokenize

input = "data/ai_hub/train.en"
output = "data/ai_hub_tok/train.en"

output_fp = open(output, "w")

with open(input) as fp:
    lines = fp.readlines()
    for idx, line in enumerate(lines):
        tok = word_tokenize(line)
        tok = ' '.join(tok)
        # print(tok)
        output_fp.write(tok+'\n')
        print(idx)

output_fp.close()