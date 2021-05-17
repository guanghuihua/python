def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    

dataSet = loadDataSet()


## 构建候选1-项集
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if [item] not in C1:
                C1.append([item]) 
    C1.sort()# [[1],[2],[3],[4],[5]]
    return list(map(frozenset, C1)) #frozenset是不可改变的集合，可以作为字典的键使用

C1 = createC1(loadDataSet())
D = list(map(set, dataSet))
minSupport = 0.5

def scanD(D, Ck, minSupport):
    ssCnt = {}  ##扫描事务数据集，统计每个候选项集的计数
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can]=1
                else:
                    ssCnt[can]+=1
    numItems = float(len(D))  ##总事务条数
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:  ##支持度大于阈值的，为频繁项集
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

L1, suppData0 = scanD(D, C1, minSupport)


def aprioriGen(Lk, k): # 频繁项集列表Lk, k为新产生的候选项集元素个数
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2];  ##k>2时，截取候选项集的前k-2项;若k=2, 则为空集
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1==L2:
                retList.append(Lk[i] | Lk[j])
    return retList

C2 = aprioriGen(L1,2)

L2, support2 = scanD(D, C2, minSupport)

def apriori(dataSet, minSupport=0.5):
    C1 = list(createC1(dataSet))
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]  #频繁1项集
    k = 2
    while len(L[k-2])>0: #L[0]对应频繁1项集
        Ck = aprioriGen(L[k-2],k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k+=1
    return L, supportData

L, suppData = apriori(dataSet, minSupport=0.5)


def calcConf(freqSet, H, supportData, br1, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf>= minConf:
            print(freqSet-conseq, '-->',conseq, 'conf:',conf)
            br1.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, br1, minConf=0.7):
    m = len(H[0])
    if len(freqSet) > m+1:
        Hmp1 = aprioriGen(H, m+1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, br1, minConf)
        if len(Hmp1)>1:
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)





def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i>1:
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList

rules = generateRules(L, suppData, minConf=0.7)



