# # import requests
# # a=requests.get('https://w3schools.com/python/demopage.htm')
# # print(a.text)

# # import requests
# # x=requests.get("http://saral.navgurukul.org/api/courses")
# # print(x.text)


# from tabnanny import check
# import requests
# import json
# from requests.api import get
# a=0
# x=requests.get('https://api.merakilearn.org/courses')
# y=x.json()
# b=json.dumps(y,indent=4)
# with open('courses.json','w') as file:
#     file.write(b)
# files = open('courses.json','r')
# c = json.load(files)
# id = []
# counter = 1
# for i in c["available courses"]:
#     print(counter,i["name"], i ["id"])
#     id.append(i["id"])
#     counter = counter + 1
# user = int(input("please enter the program no. :"))
# bitsr = id[user - 1]
# desk = requests.get('http://saral.navgurukul.org/api/courses'+bitsr'/exercise')
# yep = desk.json()
# site = json.dumps(yep,indent=4)
# with open('b.json','w') as file:
#     file.write(site)
#     now = open('b.json')
#     check = 1
#     dino = json.load(now)
#     for i in dino['data']:
#         print(check,i['name'])
#     if i['child Exercises']!=[]:
#         d = 1
#         for k in i ['child Exercise']:
#             print(' ',d,k['name'])
#             d = d + 1
#             check = check + 1
# ask = int(input('Give the topic no. :'))
# check = 1
# for i in dino['data']:
#     if check == ask:
#         if i['child Exercises'] == []:
#             see = i['slug']
#         else:
#             ask = int(input('Give the subtopic no. :'))
#             check = 1
#             for k in i['child Exercises']:
#                 if check == ask: see = k['slug']
#                 check = check + 1
#                 check = check + 1
#                 with open('child_data.json','w') as yout:

#                     desk = requests.get('http://saral.navgurukul.org/api/courses/'+bitsr+'/exercise'+'/getBySlug?slug='+see)
#                     yep = desk.json()
#                     site = json.dumps(yep,indent=4)
#                     yout.write(site)
#                     best = open('child_data.json')
#                     beta = json.load(best)
#                     print(beta['content'])






# import json
# import requests
# a=requests.get('https://api.merakilearn.org/courses')
# b=a.json()
# with open('courses.json','w') as file:
#     json.dump(b,file,indent=4)
# files=open('courses.json','r')
# read=files.read()
# data=json.loads(read)
# print()
# print("<<<<<<<<< welcome to requests >>>>>>>>>")
# print()
# i=0
# while i<len(data):
#     print(str(i+1)+".",data[i]["name"],data[i]["id"])
#     i+=1
# program=int(input("enter the program number:"))
# print(data[program-1]["name"],data[program-1]["id"])
# print()
# us=data[program-1]["name"]+"_"+data[program-1]["id"]+".json"
# s='https://api.merakilearn.org/courses'+data[program-1]["id"]+"/exersises"
# ur=requests.get(s)
# e=ur.json()
# with open(us,'w') as f:
#     json.dump(e,f,indent=4)
# new_files=open(us,'r')
# read=new_files.read()
# data=json.loads(read)
# i=0
# while i<len(data["course"]["exercises"]):
#     print(str(i+1)+".",data["course"]["exercises"][i]["name"])
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
        #     if x == "p" and program>1:
        #         print(data["course"]["exercises"][program-2]["name"],"\n")
        #         i=0
        #         while i<len(data):
        #             print(data[i]["course"]["exercises"][program-2]["cantent"][i]["value"])
        #             i=i+1
        #         program-=1
        #     else:
        #         i=0
        #         while i<len(data):
        #             print(str(i+1),data["course"]["exercises"][i]["name"])
        #             i=i+1
        # elif x!="p" and x=="n":
        #     if x=="n" and program < len(data["course"]["exercises"]):
        #         print(data["course"]["exercises"][program]["name"],"\n")
        #         i=0
        #         while i<len(data["course"]["exercises"][program-2]["content"]):
        #             print(data["course"]["exercises"][program]["content"][i]["value"])
        #             i=i+1
        #         program+=1
        #     if program == len(data["course"]["exercises"]):
        #         print("<< topic is completed >>")
        # else:
        #     print("wrong user_input")



# num=[[10],[20,30],[6,70,70,10]]

# num=[[10],[20,30],[6,70]]
# i=0
# l=[]
# while i<len(num):
#         if num[i] not in l:
#                 l.append(num[i])
#                 i=i+1
# print(l) 
                
# l=[]
# i=0
# while i<len (num):
#         if type(num[i])==list:
#                 j=0
#                 while j<len(num[i]):
#                         l.append(num[i][j])
#                         j+=1
#         else:
#                 l.append(num[i])
#         i+=1
# print(l)