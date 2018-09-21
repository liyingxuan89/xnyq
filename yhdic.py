#!/bin/env python
#coding = utf8

import pandas as pd
import pickle 


filename = 'yhDict.csv'
data = pd.read_csv(filename, sep='\t')
#print data
ids = data['id']
name = data['name']
#print ids,name

yhid = list(ids)
yhname = list(name)

id2name = dict(zip(yhid, yhname))
name2id = dict(zip(yhname, yhid))

#print id2name

with open('id2name.pkl','wb') as f1:
    pickle.dump(id2name, f1) 

with open('name2id.pkl', 'wb') as f2:
    pickle.dump(name2id, f2)


