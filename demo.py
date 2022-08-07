# http://123.57.137.208/ccf/ccf-4.jsp
from SuffixAutomaton import SuffixAutomaton, lcs1, lcs2
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
doc = raw.splitlines()
doc = [x for x in doc if x]
doc = [x.split() for x in doc]


# sam1 = SAM(doc[2])
# print(sam1)
# sam2 = SAM(s2)
# print(sam2)
# print(sam_lcs1(sam1, s2))
print(lcs1(doc[1], doc[2]))  # [['Software', 'Engineering']]
# print(sam_lcs2(sam1, doc[2:4]))
print(lcs2(doc[:4]))  # [[':'], ['on'], ['Software']]
