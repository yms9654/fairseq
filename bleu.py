from nltk.translate.bleu_score import corpus_bleu

ref = open('data/papago/ref_clean.en', 'r').read().split('\n')
hypo = open('data/papago/test_clean.en', 'r').read().split('\n')

score = corpus_bleu(ref, hypo, weights=(0.25, 0.25, 0.25, .025))
print(score)