import plotly.figure_factory as ff 
import random

dice_result=[]
for i in range(0,100):
    phone1=random.randint(1,4)
    phone2=random.randint(1,4)
    phone_result.append(phone1+phone2)

fig=ff.create_distplot([phone_result],["Result"])
fig.show()
