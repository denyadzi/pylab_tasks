# -*- coding: utf-8 -*-
import sys

def report_repeats_count(words):
    repeat_counts = {}
    for word in words:
        try:
            repeat_counts[word] += 1
        except KeyError:
            repeat_counts[word] = 1
        print "Число повторов слов введённого текста:"
        for word,count in repeat_counts.iteritems():
            print "%s: %d" % (word, count)

def report_average_sent_words_count(words_count, sents_count):
    avg_sent_words = words_count / float(sents_count)
    print "Среднее число слов в предложенях введённого текста: %.2f" % avg_sent_words

def report_median_sent_words_count(sents):
    def median(lst):
        n = len(lst)
        if n < 1:
            return None
        if n % 2 == 1:
            return sorted(lst)[n//2]
        else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0
    sent_word_counts = []
    for sent in sents:
        words_count = len(sent.strip().split())
        sent_word_counts.append(words_count)
    print "Медианное количество слов в предложенях введённого текста: %d" % median(sent_word_counts)

def ngrams_split(text, n):
    p = 0
    ngrams = []
    utext = text.decode('utf-8')
    while True:
        ngram = utext[p:p+n]
        if ngram == '' or len(ngram) < n:
            break
        p += n
        if not ngram.isalpha():
            continue
        ngrams.append(ngram)
    return ngrams

def report_topk_ngrams(topk, ngrams):
    d = {}
    for ngram in ngrams:
        try:
            d[ngram] += 1
        except KeyError:
            d[ngram] = 1
    top_ngrams = sorted(d.iteritems(), key=lambda(k,v): (v,k), reverse=True)
    print "Top-K наиболее повторяющихся буквенных N-грамм во введённом тексте:"
    for top_ngram in top_ngrams[:topk]:
        print "%s: %d" % top_ngram
        
            
print "Введите текст:"
text = sys.stdin.read()
try:
    text = text.strip()
except AttributeError:
    text = ""
if 0 == len(text):
    print "Текст не введён. Завершение программы"
    sys.exit()

print "Введите значение N для Top-K N-грамм: (N=4) "
ngramsize = 4
try:
    uservalue = sys.stdin.readline().strip()
    if uservalue != '':
        ngramsize = int(uservalue)
except ValueError:
    print "Неверное значение. Завершение программы"
    sys.exit()
    
print "Введите значение K для Top-K N-грамм: (K=10) "
topk = 10
try:
    uservalue = sys.stdin.readline().strip()
    if uservalue != '':
        topk = int(uservalue)
except ValueError:
    print "Неверное значение. Завершение программы"
    sys.exit()

if topk <= 0 or ngramsize <= 0:
    print "Значения не могут быть <= 0. Завершение программы"
    sys.exit()
    
words = text.split()
prepared = text.replace('?', '.')
prepared = prepared.replace('!', '.')
prepared = prepared.replace('...', '.')
sents  = prepared.split('.')
ngrams = ngrams_split(text, ngramsize)

report_repeats_count(words)
report_average_sent_words_count(len(words), len(sents))
report_median_sent_words_count(sents)
report_topk_ngrams(topk, ngrams)

