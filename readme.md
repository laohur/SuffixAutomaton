
# SuffixAutomaton 后缀自动机
suffix automaton by words

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
print(lcs1(doc[1], doc[2]))  # [['Software', 'Engineering']]
print(lcs2(doc[:4]))  # [[':'], ['on'], ['Software']]


```


## inspired by 
参照：https://www.cnblogs.com/shld/p/10444808.html
讲解：https://www.cnblogs.com/zjp-shadow/p/9218214.html
详解：https://www.cnblogs.com/1625--H/p/12416198.html
证明：https://oi-wiki.org/string/sam/
题解：https://www.cnblogs.com/Lyush/archive/2013/08/25/3281546.html https://www.cnblogs.com/mollnn/p/13175736.html

## feature
* suffix automaton by words 分词后缀自动机
* Longest Common Substring of two lines 两文最长共串
* Longest Common Substring of document 多文最长共串
