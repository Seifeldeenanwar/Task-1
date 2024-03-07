while True:
#this function about problem 2 we take a number and check if number Armstrong or not
 def check_Armstrong():
  while True :
   try:
    num=input('insert any positive integar')
    while int(num) < 0:
     num=input('please, insert correct positive number')
    ind=0
    time=0
    result=0
    while len(num)>time:
     result+=int(num[ind])**len(num)
     time+=1
     ind+=1
    if result==int(num):
     print(num,"is Armstrong ")
     break
    else: 
     print(num,"not Armstrong")
     break
   except:
    print("insert a valid input")
   
# the following function about problem 1 we will take mark from user and display his grade  
 def Grades() :
  while True:
   try:
    mark=int(input('insert your mark'))
    while mark > 100 or mark < 0 :
     mark=int(input('insert a right mark'))
    if mark >= 90  :
     print("A+")
     break
    elif mark >= 85 :
     print("A")
     break
    elif mark >= 80 :
     print("B+")
     break
    elif mark >= 75 :
     print("B")
     break
    elif mark >= 70 :
     print("C+")
     break
    elif mark >= 65 :
     print("C")
     break
    elif mark >= 60:
     print("D+")
     break
    elif mark >= 50 :
     print("D")
     break
    else:
     print("F")
     break
   except:
    print("please, insert a valid number")
   
#choose_service is a variable which make us know what user uses program to
 choose_service = input('choose A)Armstrong  B)Grades C)End program ') .upper()
 while choose_service not in ["A" , "B" , "C"] :
  choose_service = input ('please, select a valid choise') .upper()
 if choose_service == "A" :
  check_Armstrong()
 elif choose_service == "B" :  
  Grades()
 elif choose_service == "C" :
  print ("Exit program")
  break