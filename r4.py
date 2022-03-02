# import json,requests
# requests_file=requests.get('https://api.merakilearn.org/courses').json()
# with open('courses.json','w') as files:
#     json.dump(requests_file,files,indent=4)
# file_data=open('courses.json','r').read()
# data=json.loads(file_data)
# print()
# print("<<<<<<<<< welcome to requests >>>>>>>>>")
# print()
# i=0
# while i<len(data):
#     print(str(i+1)+".",data[i]["name"],data[i]["id"])
#     i+=1
# program=int(input("enter the program number:"))
# print(data[program-1]["name"],data[program-1]["id"])

# program_file=data[program-1]["name"]+"_"+data[program-1]["id"]+".json"
# pro_file='https://api.merakilearn.org/courses'+data[program-1]["id"]+"/exersises"
# program_files=requests.get(pro_file).json()
# with open(program_files,'w') as program_data:
#     json.dump(program_files,program_data,indent=4)
# new_files=open(program_files,'r').read()
# data=json.loads(new_files)
# i=0
# while i<len(data["course"]["exercises"]):
#     print(str(i+1)+")" ,data["course"]["exercises"][i]["name"])
#     i=i+1
# top=int(input("enter the topic_number:"))
# i=0
# while i<len(data["course"]["exercise"][top-1]["content"]):
#     print(data["course"]["exercise"][top-1]["content"][i]["value"])
#     print()
#     i=i+1
# i=0
# while i<len(data["course"]["exercise"][top-1]["content"]):
#     due=input("choose your previous or next (p and n):--")
#     if due=="p":
#         print(data["course"]["exercise"][top-2]["content"][i]["value"])
#     if due=="n":
#         print(data["course"]["exercise"][top]["content"][i]["value"])
#         break
#     i=i+1
# i=0
# while i<len(data):
#         x=input("enter the previous or next(p and n):--")
#         if x!= "n" and x=="p":
#             if x == "p" and program>1:
#                 print(data["course"]["exercises"][program-2]["name"],"\n")
#                 i=0
#                 while i<len(data):
#                     print(data[i]["course"]["exercises"][program-2]["cantent"][i]["value"])
#                     i=i+1
#                 program-=1
#             else:
#                 i=0
#                 while i<len(data):
#                     print(str(i+1),data["course"]["exercises"][i]["name"])
#                     i=i+1
#         elif x!="p" and x=="n":
#             if x=="n" and program < len(data["course"]["exercises"]):
#                 print(data["course"]["exercises"][program]["name"],"\n")
#                 i=0
#                 while i<len(data["course"]["exercises"][program-2]["content"]):
#                     print(data["course"]["exercises"][program]["content"][i]["value"])
#                     i=i+1
#                 program+=1
#             if program == len(data["course"]["exercises"]):
#                 print("<< topic is completed >>")
#         else:
#             print("wrong user_input")

















#   from asyncore import read
# import json
# import requests

# a=requests.get('https://api.merakilearn.org/courses')
# b=a.json()
# with open("meraki.json","w") as file:
#     json.dump(b,file,indent=4)
# r=open("meraki.json","r")
# read=r.read()
# data=json.loads(read)
# print(type(data))
# print(data)
# c=1
# # n=int(input("enter which course do u want:"))
# for i in data:
#     print(str(c)+")",i["name"])
#     c=c+1
# # x=requests.get('https://api.merakilearn.org/courses/'+b[i]["id"]+''+'/exercise')
# x=requests.get('https://api.merakilearn.org/courses/74/exercises')
# d=x.json()
# with open("course.json","w") as files:
#     json.dump(d,files,indent=4)
# v=[]
# with open("course.json","r") as new_file:
#     p=json.load(new_file)
#     t=1
#     for n in p["course"]["exercises"]:
#         print(t,n["name"])
#         v.append(n["slug"])
#         t=t+1
# user=int(input("enter the program number:-"))
# o=requests.get('https://saral.navgurukul.org/api/courses/74/exercise/getBySlug?slug')
# k=o.json()
# print(k)
# with open("last_data.json","w") as fil:
#     json.dump(k,fil,indent=4)              