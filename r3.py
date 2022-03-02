# from asyncore import read
# from itertools import count
import json
import requests

a=requests.get('https://api.merakilearn.org/courses')
b=a.json()
with open("meraki.json","w") as file_s:
    json.dump(b,file_s,indent=4)
read_file=open("meraki.json","r")
read=read_file.read()
data=json.loads(read)
print(type(data))
print(data)
count=1
for i in data:
    print(str(count)+")",i["name"])
    count=count+1
next=requests.get('https://api.merakilearn.org/courses/str()74/exercises')
d=next.json()
with open("course.json","w") as files:
    json.dump(d,files,indent=4)
list=[]
with open("course.json","r") as new_file:
    pee=json.load(new_file)
    text=1
    for num in pee["course"]["exercises"]:
        print(text,num["name"])
        list.append(num["slug"])
        text=text+1
user=int(input("enter the program number:-"))
ox=requests.get('https://saral.navgurukul.org/api/courses/74/exercise/getBySlug?slug')
key=ox.json()
print(key)
with open("last_data.json","w") as fil:
    json.dump(key,fil,indent=4)























# user1= str(input("enter your direction:"))
# if user1 == "up":
#     print(user)
# elif user1=="p":
#     user=user-1
#     print(user)
# elif user1=="n":
#     user=user+1
#     print(user)
# else:
#     print(user)


