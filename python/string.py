##string function
str = "i am a mobashara"
print(str.upper())
print(str.lower())
a = " Aymana, mobashara!"
print(a.strip()) # he strip() method removes any whitespace from the beginning or the end:
##replace() method replaces a string with another string
print(a.replace("s", "k"))#jake replace korbo se prothome jeta diye replace korbo seta sesh e
##python boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)
##practice tkae input from user and print the length
name=input("enter your name:")
print("length of name is",len(name))
str="mobashara"
print(str.count("o"))
##conditional statement
light="red"
if(light=="green"):
    print("stop")
elif(light=="red"):
    print("tata by by")
    num=5
    if(num>2):
        print("grater than 2")
        #light="purple"
#if(light=="green"):
   # print("stop")
#elif(light=="red"):
  #  print("tata by by")
#else:
   # print("light is broken")
age=14
if(age>=21):
        print("can vote")
else:
 print("cannot vote")