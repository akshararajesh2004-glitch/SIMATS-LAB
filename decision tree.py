import math
from collections import Counter

data=[['Sunny','High','No'],['Sunny','Normal','Yes'],
      ['Overcast','High','Yes'],['Rain','High','Yes'],
      ['Rain','Normal','No'],['Overcast','Normal','Yes']]
attrs=['Outlook','Humidity']

def entropy(ex):
    lbl=[r[-1] for r in ex]; t=len(lbl)
    return -sum((c/t)*math.log2(c/t) for c in Counter(lbl).values()) 

def info_gain(ex,i):
    t=entropy(ex)
    return t - sum((len([r for r in ex if r[i]==v])/len(ex))*entropy([r for r in ex if r[i]==v]) for v in set(r[i] for r in ex))

def id3(ex,attr):
    lbl=[r[-1] for r in ex]
    if lbl.count(lbl[0])==len(lbl): return lbl[0]
    if not attr: return Counter(lbl).most_common(1)[0][0]
    best_i=[info_gain(ex,i) for i in range(len(attr))].index(max([info_gain(ex,i) for i in range(len(attr))]))
    tree={attr[best_i]:{}}
    for v in set(r[best_i] for r in ex):
        subset=[r[:best_i]+r[best_i+1:] for r in ex if r[best_i]==v]
        tree[attr[best_i]][v]=id3(subset,attr[:best_i]+attr[best_i+1:])
    return tree

print("Decision Tree:\n",id3(data,attrs))
