import re

# 1、读取文件内容
f = open('Walden.txt',mode='r')
rare_words = f.read()

# 2、文件内容整理
m_words = rare_words.lower()
new_words = re.sub('[,."\'\n?;!]', '',m_words)
words = new_words.split()

# 3、词频统计
word_freq = {}
for word in words:
    if word not in word_freq.keys():
        word_freq[word] = 1
    else:
        word_freq[word] += 1

# 4、词频排序
result = sorted(word_freq.items(),key=lambda x:x[1],reverse=True)
result_str = str(result)

# 5、写入内容
with open('result.txt',mode='w') as f:
    f.write(result_str)