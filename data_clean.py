lang = 'en'
dir = 'papago'

input = f'data/{dir}/ref.{lang}'
output = open(f'data/{dir}/ref_clean.{lang}', 'w')

def clean(line):
    ret = line.replace('>', '')
    ret = ret.replace('<', '')
    ret = ret.replace('/', '')
    ret = ret.replace('”', '"')
    ret = ret.replace('“', '"')
    ret = ret.replace('…', '')
    ret = ret.replace('’', '`')
    ret = ret.replace('‘', '\'')
    ret = ret.strip()
    ret = ret.lower()
    # print(input, ret)
    return ret

with open(input, 'r') as fp:
    for idx, line in enumerate(fp):
        line = clean(line)
        output.write(line+'\n')        
        print(idx)

output.close()