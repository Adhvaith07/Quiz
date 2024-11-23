# Quiz program time limit....
import time
score=0
def timer():
    a=time.time()
    value=input("Answer: ")
    b=time.time()
    c=b-a
    if 5<=c:
       print("You have run out of time...")
       return 0
    else:
       return value

def quest(a,b):
    score=0
    if a==b:
        print("Correct Answer !")
        score+=50
    else:
        print("Incorrect Answer !")
    return score
       
print("\nFirst Question...")       
print("Who is father of computer\n")
print("\tA.Charles Babbage\n\tB.Rabindranath Tagore\n\tC.Mahatma Ganghi\n\tD.Pele ")
first=timer()
score+=quest(first,'A')
print()

print("Second Question...")
print("5 + 5 =")
print("\tA. 0\n\tB. 10\n\tC. 100 \n\tD. 01")
second=timer()
score+=quest(second,'B')

print("\tYour total score:",score)
