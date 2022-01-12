import random 
import plotly.express as px
count=[]
phone_result=[]
for i in range(0,100):
    phone1=random.randint(1,4)
    phone2=random.randint(1,4)
    phone_result.append(phone1+phone2)
    count.append(i)


print(count,phone_result)

fig=px.bar(x=phone_result,y=count)
fig.show()
