import linecache
import random

full_en = 'data/ai_hub_sp/clean.en'
full_ko = 'data/ai_hub_sp/clean.ko'

train_en = open('data/ai_hub_sp/train.en', 'w')
train_ko = open('data/ai_hub_sp/train.ko', 'w')
valid_en = open('data/ai_hub_sp/valid.en', 'w')
valid_ko = open('data/ai_hub_sp/valid.ko', 'w')
test_en = open('data/ai_hub_sp/test.en', 'w')
test_ko = open('data/ai_hub_sp/test.ko', 'w')

test_size = 0
with open(full_en, 'r') as fp:
    for idx, en in enumerate(fp):
        ko = linecache.getline(full_ko, idx+1)
        if idx % 10 == 0:
            if random.choice([True, False]) and test_size < 5000:
                test_en.write(en)
                test_ko.write(ko)
                test_size+=1
            else:
                valid_en.write(en)
                valid_ko.write(ko)
        else:
            train_en.write(en)
            train_ko.write(ko)

train_en.close()
train_ko.close()
valid_en.close()
valid_ko.close()
test_en.close()
test_ko.close()