lang = 'ko'
name = 'test'

input = f'data/{name}/full.{lang}'
output = open(f'data/{name}/clean.{lang}', 'w')

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