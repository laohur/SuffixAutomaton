
# SuffixAutomaton 后缀自动机
find LCS (longest common substrings) by suffix automaton 

## usage
> pip install SuffixAutomaton 

```python
from SuffixAutomaton import SuffixAutomaton, lcs1, lcs2, logger

raw = """
ASE : International Conference on Automated Software Engineering
ESEC/FSE : ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering
ICSE : International Conference on Software Engineering
ISSTA : The International Symposium on Software Testing and Analysis
OOPSLA : Conference on Object-Oriented Programming Systems, Languages, and Applications
OSDI : Operating Systems Design and Implementation
PLDI : ACM SIGPLAN conference on Programming Language Design and Implementation
POPL : ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages
SOSP : ACM Symposium on Operating Systems Principles
"""
doc = raw.strip().splitlines()
doc = [x.split() for x in doc]
# for tokens
logger.info(lcs1(doc[1], doc[2], output_lcs=True))  # [(14, 2, 5, ['Software', 'Engineering'])]
logger.info(lcs2(doc[0], doc[1:4], output_lcs=True))  # [(1, 1, [':']), (4, 1, ['on']), (6, 1, ['Software'])]
logger.info(lcs1(doc[1], doc[2], 1, output_lcs=True)) # [(1, 1, 1, [':']), (7, 1, 3, ['Conference']), (10, 1, 4, ['on']), (14, 2, 5, ['Software', 'Engineering'])]
logger.info(lcs2(doc[0], doc[1:4], 1, output_lcs=True)) # [(1, 1, [':']), (4, 1, ['on']), (6, 1, ['Software'])]
logger.info(lcs2(doc[0], doc[1:4], 1, output_lcs=False)) # [(1, 1, None), (4, 1, None), (6, 1, None)]

# for chars
poet = "江天一色无纤尘皎皎空中孤月轮 江畔何人初见月江月何年初照人 人生代代无穷已江月年年望相似 不知江月待何人但见长江送流水"
doc = poet.split()   
logger.info(lcs1(doc[1], doc[3], output_lcs=True))  #  [(2, 2, 5, '何人'), (7, 2, 2, '江月')]
logger.info(lcs1(doc[1], doc[3], 1, output_lcs=True)) # [(0, 1, 10, '江'), (2, 2, 5, '何人'), (5, 1, 8, '见'), (7, 2, 2, '江月')]
# for lcs of doc
logger.info(lcs2(doc[2], doc[2:4], output_lcs=True))  # [(7, 2, '江月')]
logger.info(lcs2(doc[2], doc[2:4], 1 ,output_lcs=True)) # [(0, 1, '人'), (7, 2, '江月')]
# faster when iterally
sam = SuffixAutomaton(doc[0])
for x in doc[1:]:
    print((x, sam.lcs1(x, output_lcs=True)))
"""
('江畔何人初见月江月何年初照人', [(0, 1, 0, '江'), (12, 1, 6, '月')])
('人生代代无穷已江月年年望相似', [(0, 1, 7, '江'), (4, 1, 4, '无'), (12, 1, 8, '月')])
('不知江月待何人但见长江送流水', [(0, 1, 2, '江'), (12, 1, 3, '月')])
"""

# lcs() -> [(str, start, cand_start)], sort in length decending. may overlap. 
logger.info(lcs2("布架 拖把抹布悬挂沥水洁具架 ", ["抹布架"], 1, output_lcs=True))  # [(0, 2, '布架'), (5, 2, '抹布'), (13, 1, '架')]


```

## feature
* suffix automaton [in words] 可分词后缀自动机
* [Longest] Common Substring of two lines 两文[最长]共串
* [Longest] Common Substring of document 多文[最长]共串


## inspired by 
    参照：https://www.cnblogs.com/shld/p/10444808.html
    讲解：https://www.cnblogs.com/zjp-shadow/p/9218214.html
    详解：https://www.cnblogs.com/1625--H/p/12416198.html
    证明：https://oi-wiki.org/string/sam/
    题解：https://www.cnblogs.com/Lyush/archive/2013/08/25/3281546.html https://www.cnblogs.com/mollnn/p/13175736.html
