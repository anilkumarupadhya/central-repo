###programe to find the Factorial of a user input number
print("give input of a number for factorial")
import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
text=''
factorial=1
while(True):
    print("give a choice for run program or break program")
    choice=int(input("enter 1/2 "))
    if choice == 1:

        def speak():
    
            engine.runAndWait()

        text="enter number for factorial"
        engine.say(text)
        speak()
        num=int(input('enter number for factorial'))
        def factorial_of_num():
            factorial=1
            for fact in range(1,num+1):
                factorial=factorial*fact
            print(factorial)
            engine.say(f"your number of factorial is {factorial}")
            speak()
        factorial_of_num()
    elif choice==2:
        break

        
