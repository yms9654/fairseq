import linecache

train_size = 500000
val_size = 50000
test_size = 5000

full_en = 'data/ai_hub/clean.en'
full_ko = 'data/ai_hub/clean.ko'

with open(full_en, 'r') as fp:
    for idx, en in enumerate(fp):
        ko = linecache.getline()
        
        
