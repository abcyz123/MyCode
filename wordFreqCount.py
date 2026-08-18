# 1、把所有单词变成小写
# 2、分词
# 3、统计次数

word = "Hello new world, hello old world "
new_words = word.lower()
words_list = new_words.split()
words = {}

for i in words_list:
    if i in words.keys():
        words[i] += 1
    else:
        words[i] = 1

print(words)
