import linecache

full_en = 'data/ai_hub/full.en'
full_ko = 'data/ai_hub/full.ko'

output_en = open('data/ai_hub/clean.en', 'w')
output_ko = open('data/ai_hub/clean.ko', 'w')

def clean(input):
    ret = input.replace('>', '')
    ret = ret.strip()
    # print(input, ret)
    return ret

with open(full_en, 'r') as fp:
    for idx, en in enumerate(fp):
        en = clean(en)
        output_en.write(en+'\n')

        ko = linecache.getline(full_ko, idx+1)
        ko = clean(ko)
        output_ko.write(ko+'\n')

        print(idx)

output_en.close()
output_ko.close()