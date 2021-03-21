import physbo
import numpy as np
from sklearn.preprocessing import OneHotEncoder


# データ読み込み
def load_data():
    A =  np.asarray(np.loadtxt('data/s5-210.csv',skiprows=1, delimiter=',') )
    X = A[:,0:3]
    t  = -A[:,3]
    return X, t

X, t = load_data()
X = physbo.misc.centering(X) #標準化

#%%
# 探索領域設定
x=[]
categ=[]
x.append(np.linspace(0, 1, 101))#離散変数
categ.append(0)
x.append(np.linspace(0, 1, 101))#離散変数
categ.append(0)
x.append(np.linspace(0, 2, 3))
categ.append(1)

xlist=[]
for i in range(len(x)):
    xlist.append(x[i])

SS=np.array(np.meshgrid(*xlist,indexing='ij')).reshape([len(x),-1]).transpose()
enc = OneHotEncoder(categories="auto", sparse=False, dtype=np.float32)
SS_e=np.zeros([SS.shape[0],0])
e_flag=np.zeros([0])
categ_num=0
for i in range(len(x)):
    if categ[i]==1:
        categ_num+=1
        SS_onehot=enc.fit_transform(SS[:,i:i+1])
        SS_e=np.hstack([SS_e,SS_onehot])
        e_flag=np.hstack([e_flag,categ_num*np.ones([SS_onehot.shape[1]])])
    else:
        SS_e=np.hstack([SS_e,SS[:,i:i+1]])
        e_flag=np.hstack([e_flag,0])



#%%
# インデックス探索
calculated_ids=[]
for j in range(X.shape[0]):
    pos=1
    for i in range(X.shape[1]):
        pos*=(SS[:,i]==X[j,i])
    calculated_ids.append(np.where(pos==1)[0][0])
calculated_ids=np.array(calculated_ids)

# policy のセット
policy = physbo.search.discrete.policy(test_X=SS_e, initial_data=[calculated_ids, t])

# シード値のセット
policy.set_seed( 0 )

#actions = policy.random_search(max_num_probes=1, simulator=None)
actions = policy.bayes_search(max_num_probes=1, simulator=None, score='EI', interval=0,  num_rand_basis = 5000)
next_param=SS[actions,:]

