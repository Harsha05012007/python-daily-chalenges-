import random, pandas as pd, numpy as np, math
import matplotlib.pyplot as plt

def generate_data(n):
    return [(i,
             random.randint(0,100),
             random.randint(0,100),
             random.randint(0,50),
             (lambda m,a,asgn:(m*0.6+asgn*0.4)*math.log(a+1))
             (random.randint(0,100),random.randint(0,100),random.randint(0,50)))
            for i in range(1,n+1)]

def classify_students(df):
    d={"At Risk":[],"Average":[],"Good":[],"Top Performer":[]}
    for _,r in df.iterrows():
        if r.marks<40 or r.attendance<50: d["At Risk"].append(r.student_id)
        elif 40<=r.marks<=70: d["Average"].append(r.student_id)
        elif 71<=r.marks<=90: d["Good"].append(r.student_id)
        elif r.marks>90 and r.attendance>80: d["Top Performer"].append(r.student_id)
    return d

def analyze_data(df):
    m=np.array(df.marks)
    mean=sum(m)/len(m)
    med=np.median(m)
    std=np.std(m)
    mn,mx=min(m),max(m)
    df["normalized"]=[(x-mn)/(mx-mn) for x in m]
    corr=np.corrcoef(df.marks,df.attendance)[0][1]
    return mean,med,std,corr,mx

def detect(df,std,c):
    res=[]
    if std<15: res.append("Stable Academic System")
    if len(df[df.attendance<50])>3: res.append("Critical Attention Required")
    else: res.append("Moderate Performance")
    if len(c["Top Performer"])>=2: res.append("High Achievement")
    return res

n=5
data=generate_data(n)
df=pd.DataFrame(data,columns=["student_id","marks","attendance","assignment","pi"])

cat=classify_students(df)
mean,med,std,corr,mx=analyze_data(df)
ins=detect(df,std,cat)

print(df)
print(cat)
print((mean,std,mx))
print(ins)

plt.hist(df.marks)
plt.show()