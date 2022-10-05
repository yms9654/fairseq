import linecache

input = 'data/teracomix/full.ko'

output = open('data/teracomix/clean.ko', 'w')

def clean(input):
    ret = input.replace('>', '')
    ret = ret.replace('<', '')
    ret = ret.replace('/', '')
    ret = ret.replace('”', '"')
    ret = ret.replace('“', '"')
    ret = ret.replace('…', '')
    ret = ret.strip()
    # print(input, ret)
    return ret

with open(input, 'r') as fp:
    for idx, line in enumerate(fp):
        line = clean(line)
        output.write(line+'\n')        
        print(idx)

output.close()