import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# strip() 方法用于移除字符串头尾指定的字符（默认为空格）。str.strip([chars])
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

# capitalize()将字符串的第一个字母变成大写,其他字母变小写。str.capitalize()
# random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。random.sample(str, num)
# count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。str.count(sub, start= 0, end=len(string))
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

# random.randint()生成一个指定范围的随机整数。random.randint(a,b)
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

# replace()方法把字符串中的old（旧字符串）替换成new(新字符串)，如果指定第三个参数max，则替换不超过max次。str.replace(old, new[, max])
    for sentence in snippet, phrase:
        result = sentence[:]
        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other name
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until the hit CTRL-D
# random.shuffle() 方法将序列的所有元素随机排序。random.shuffle(lst)
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input(">")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"