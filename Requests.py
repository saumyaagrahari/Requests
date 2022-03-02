import json, requests

data = requests.get("https://api.merakilearn.org/courses").json()

with open("meraki.json","w") as courses:       #create file
  json.dump(data, courses, indent=4)          # dump data to file of json

course_file = open("meraki.json","r").read()  # open and read file
data = json.loads(course_file)                #load data to a variable

list_of_data = []
count = 1

for i in data:
  print(count,">>>", i["name"])
  list_of_data.append(i["id"])
  count=count+1

user_input_1 = int(input("Enter course no which you want to choose >>>  "))
exercises_data = requests.get('https://api.merakilearn.org/courses/'+ str(list_of_data[user_input_1 - 1]) +'/exercises').json()

with open("course.json","w") as exercises:
    json.dump(exercises_data, exercises, indent=4)

course_file = open("course.json","r")  # open and read file
data = json.load(course_file)

print(data)

slug_data = []
count = 1

for num in data["course"]["exercises"]:
  print(count, num["name"])
  slug_data.append(num['slug'])
  count += 1

user_input_2 = int(input("Enter course slug no which you want to choose >>>  "))

slug_data_request = requests.get('https://saral.navgurukul.org/api/courses/'+ str(list_of_data[user_input_1 - 1]) +'/exercise/getBySlug?slug='+ str(slug_data[user_input_2 - 1])).json()

with open("slug_data.json","w") as slug_data_file:
    json.dump(slug_data_request, slug_data_file, indent=4)

slug_of_course_file = open("slug_data.json","r")  

data = json.load(slug_of_course_file)

print(data)

pto = ("""do you want to continue or go next or previous one. Please select one of these >>>
0 >>>  continue
1 >>> next
2 >>> previous""")
if pto == 1:
  slug_data_request = requests.get('https://saral.navgurukul.org/api/courses/'+ str(list_of_data[user_input_1]) +'/exercise/getBySlug?slug='+ str(slug_data[user_input_2 - 1])).json()
elif pto == 2:
  slug_data_request = requests.get('https://saral.navgurukul.org/api/courses/'+ str(list_of_data[user_input_1 - 2]) +'/exercise/getBySlug?slug='+ str(slug_data[user_input_2 - 1])).json()
elif pto == 0:
  pass























# option = ("""do you want choice next or previous. please select one of these >>> 
# 1 >>> next
# 2 >>> previous""")
# if option == 1:
#   option_data = requests.get('https://api.merakilearn.org/courses/'+ str(list_of_data[user_input_1 - 1]) +'/exercises').json()
# elif option == 2:
#   option_data = requests.get('https://api.merakilearn.org/courses/'+ str(list_of_data[user_input_1]) +'/exercises').json()
# else:
#   print("please enter correct choice !!!") 


# else:
#   print("Please enter correct choice !!!")


  # if slug_data_request:
    # pass
    # with open("slug_data.json","w") as slug_data_file:
    #   json.dump(slug_data_request, slug_data_file, indent=4)
    # slug_of_course_file = open("slug_data.json","r")  
    # data = json.load(slug_of_course_file)
# elif pto == 0:
#   pass
# else:
#   print("Please enter correct choice !!!")
