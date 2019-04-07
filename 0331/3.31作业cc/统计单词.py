f = open("Half a day.txt", "r",encoding='utf-8').read()
words_num = len(f.split())
print("单词数量%s"%(words_num))

