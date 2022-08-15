
# SuffixAutomaton 后缀自动机
suffix automaton by words, to get text common substrings and simularity


## usage
> pip install SuffixAutomaton 

```python
raw = """
    ASE : International Conference on Automated Software Engineering
    ESEC/FSE : ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
    ICSE : International Conference on Software Engineering
    ISSTA : The International Symposium on Software Testing and Analysis
    """
doc = raw.splitlines()
doc = [x for x in doc if x]
doc = [x.split() for x in doc]

from SuffixAutomaton import SuffixAutomaton,lcs1,lcs2
# tokenize in words
# longest
# [(['Software', 'Engineering'], 14, 5)]
print(lcs1(doc[1], doc[2]))
print(getSimularity(doc[1], doc[2]))  # 0.39355199883902836
# [([':'], 1), (['on'], 4), (['Software'], 6)]
print(lcs2(doc[0], doc[1:4]))

# tokenize in chars
# all common substrings
poet = "江天一色无纤尘皎皎空中孤月轮 江畔何人初见月江月何年初照人 人生代代无穷已江月年年望相似 不知江月待何人但见长江送流水"
doc = poet.split()
# [(['江'], 0, 10), (['何', '人'], 2, 5), (['见'], 5, 8), (['江', '月'], 7, 2)]
print(lcs1(doc[1], doc[3], 1))
# [(['人'], 0), (['江', '月'], 7)]
print(lcs2(doc[2], doc[2:4], 1))
print(getSimularity("大话西游", "大话西游手游"))  # 0.8513286423569945


```

## feature
* suffix automaton [in words] 可分词后缀自动机
* [Longest] Common Substring of two lines 两文[最长]共串
* [Longest] Common Substring of document 多文[最长]共串
* getSimularity by ChangEntropy 文本近似度计算


## inspired by 
    参照：https://www.cnblogs.com/shld/p/10444808.html
    讲解：https://www.cnblogs.com/zjp-shadow/p/9218214.html
    详解：https://www.cnblogs.com/1625--H/p/12416198.html
    证明：https://oi-wiki.org/string/sam/
    题解：https://www.cnblogs.com/Lyush/archive/2013/08/25/3281546.html https://www.cnblogs.com/mollnn/p/13175736.html
    相似度: https://www.cnblogs.com/huilixieqi/p/6493089.html http://groups.di.unipi.it/~bozzo/The%20Harmonic%20Mean.htm
