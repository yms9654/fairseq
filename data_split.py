import linecache
import random

path = 'data/tc_wt/'

full_en = path+'clean_sp.en'
full_ko = path+'clean_sp.ko'

train_en = open(path+'train.en', 'w')
train_ko = open(path+'train.ko', 'w')
valid_en = open(path+'valid.en', 'w')
valid_ko = open(path+'valid.ko', 'w')
test_en = open(path+'test.en', 'w')
test_ko = open(path+'test.ko', 'w')

test_size = 0
max_test_size = 500
# valid + test 데이터 사이즈를 10%로 만들고 test 데이터는 max_test_size 만큼 만든다.
with open(full_en, 'r') as fp:
    for idx, en in enumerate(fp):
        ko = linecache.getline(full_ko, idx+1)
        if idx % 10 == 0:            
            if random.choice([True, False]) and test_size < max_test_size:
                test_en.write(en)
                test_ko.write(ko)
                test_size+=1
            else:
                valid_en.write(en)
                valid_ko.write(ko)
        else:
            train_en.write(en)
            train_ko.write(ko)
        print(idx)

train_en.close()
train_ko.close()
valid_en.close()
valid_ko.close()
test_en.close()
test_ko.close()