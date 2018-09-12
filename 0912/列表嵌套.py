import random
techers=["chenyang",'liudehua','wangwei','yangzhenying','wuyifan','sunwukong','lifangyue','yangjie']
offices=[[],[],[]]

for tencher in techers:
    num = random.randint(0,2)
    offices[num].append(tencher)
print(offices)
for office in offices:
    print("该办公室共有%d人，他们是: " % len(office))
    for i in office:
        print(i)