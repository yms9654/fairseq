import linecache

lang = 'en'
input = f'data/ai_hub/full.{lang}'

output = open(f'data/ai_hub/clean.{lang}', 'w')

def clean(input):
    ret = input.replace('>', '')
    ret = ret.replace('<', '')
    ret = ret.replace('/', '')
    ret = ret.replace('”', '"')
    ret = ret.replace('“', '"')
    ret = ret.replace('…', '')
    ret = ret.replace('’', '`')
    ret = ret.replace('‘', '\'')
    ret = ret.strip()
    # print(input, ret)
    return ret

with open(input, 'r') as fp:
    for idx, line in enumerate(fp):
        line = clean(line)
        output.write(line+'\n')        
        print(idx)

output.close()