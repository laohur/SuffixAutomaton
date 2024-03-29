from SuffixAutomaton import SuffixAutomaton,lcs1,lcs2
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
print(lcs1(doc[1], doc[2]))  # [(['Software', 'Engineering'], 14, 5)]
print(lcs2(doc[0], doc[1:4]))  # [([':'], 1), (['on'], 4), (['Software'], 6)]
print(lcs1(doc[1], doc[2], 1)) # [([':'], 1, 1), (['Conference'], 7, 3), (['on'], 10, 4), (['Software', 'Engineering'], 14, 5)]
print(lcs2(doc[0], doc[1:4], 1)) # [([':'], 1), (['on'], 4), (['Software'], 6)]

# for chars
poet = "江天一色无纤尘皎皎空中孤月轮 江畔何人初见月江月何年初照人 人生代代无穷已江月年年望相似 不知江月待何人但见长江送流水"
doc = poet.split()   
print(lcs1(doc[1], doc[3]))  #  [('何人', 2, 5), ('江月', 7, 2)]
print(lcs1(doc[1], doc[3], 1)) # [('江', 0, 10), ('何人', 2, 5), ('见', 5, 8), ('江月', 7, 2)]
# for lcs of doc
print(lcs2(doc[2], doc[2:4]))  # [('江月', 7)]
print(lcs2(doc[2], doc[2:4], 1)) # [('人', 0), ('江月', 7)]
# faster when iterally
sam=SuffixAutomaton(doc[0])
for x in doc[1:]:
    print((x,sam.lcs1(x)))
"""
('江畔何人初见月江月何年初照人', [('江', 0, 0), ('月', 12, 6)])
('人生代代无穷已江月年年望相似', [('江', 0, 7), ('无', 4, 4), ('月', 12, 8)])
('不知江月待何人但见长江送流水', [('江', 0, 2), ('月', 12, 3)])
"""

# lcs() -> [(str, start, cand_start)], sort in length decending. may overlap. 
print(lcs2("布架 拖把抹布悬挂沥水洁具架 ", ["抹布架"], 1))  # [('布架', 0), ('抹布', 5), ('架', 13)]
