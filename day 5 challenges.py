name = input("Enter your full name: ")
no_space = ""
for ch in name:
    if ch != " ":
        no_space = no_space + ch

n=int(input("enter number of requests :"))
res_req=[0]*n
for i in range(n):
    res_req[i]=int(input("enter requests :"))
low_demand=[0]*n
moderate_demand=[0]*n
high_demand=[0]*n
invalid_requests=[0]*n
no_demand=[0]*n
ld=0
md=0
hd=0
nd=0
ir=0
rc=0
valid=0
for i in res_req:
    if i < 0:
        invalid_requests[ir]=i
        ir+=1
    else:
        valid+=1
        if i==0:
            no_demand[nd]=i
            nd+=1
        elif i>=1 and i<=20:
            low_demand[ld]=i
            ld+=1
        elif i>=21 and i<=50:
            moderate_demand[md]=i
            md+=1
        elif i>50:
            high_demand[hd]=i
            hd+=1
print("before filtering:")
print("low_demand:",low_demand[:ld])
print("moderate_demand:",moderate_demand[:md])
print("high_demand:",high_demand[:hd])
print("no_demand:",no_demand[:nd])
print("invalid_requests:",invalid_requests[:ir])
print("After filtering")
l=len(no_space)
PLI=l%3
if PLI==0:
    rc=ld
    ld=0
    rule="Rule A applied"
elif PLI==1:
    rc=hd
    hd=0
    rule="Rule B applied"
elif PLI==2:
    rc+=ld
    ld=0
    rc+=hd
    rc+=ir
    ir=0
    hd=0
    rc += nd
    nd = 0
    rule="Rule C applied"
removed=rc
print("L value =",l)
print("PLI value =",PLI)
print("total removed due to PLI ",removed)
print("After filtering:")
print(rule)
print("low_demand:",low_demand[:ld])
print("moderate_demand:",moderate_demand[:md])
print("high_demand:",high_demand[:hd])
print("invalid_requests:",invalid_requests[:ir])
print("total valid requests:",valid)





