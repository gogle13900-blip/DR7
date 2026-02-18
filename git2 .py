import pandas as pd
r=pd.read_csv("user.csv")#your addres
# توضیح 
#for index,row in r.iterrows():
  #ردیف و ستون
s1=r.iloc[:,1]
s2=r.iloc[:,0]
#add.move
with open('move.txt','w',encoding='utf_8')as f :
  for index,row in r.iterrows():
        if row["ps"]==".move":
          #add.music
            f.write(row['name']+'\n')
with open('music.txt','w',encoding='utf_8')as f :
  for index,row in r.iterrows():
        if row["ps"]==".music":
            f.write(row['name']+'\n')
#add.code
with open('code.txt','w',encoding='utf_8')as f :
  for index,row in r.iterrows():
        if row["ps"]==".code":
            f.write(row['name']+'\n')
#add.js
with open('js.txt','w',encoding='utf_8')as f :
  for index,row in r.iterrows():
        if row["ps"]==".js":
            f.write(row['name']+'\n')
#بقیه رو بریزه یک جای دیگه
        

    
