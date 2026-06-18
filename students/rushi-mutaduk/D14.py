subjects=3
pass_marks=35
distingtion_marks=75
n=0
def print_marks(name,mark1,mark2,mark3):
    total=mark1+mark2+mark3
    avrage=total/subjects
    global n
    n=n+1
    print("="*12,f"REPORT  CARD - {n}","="*12)
    print("name :",name)
    print("total marks :",total)
    print("avrage/percentage",avrage)
    if avrage>distingtion_marks:
        print("congratulation! pass with distingtion ")
    elif avrage<pass_marks:
        print("Failed")
    else:#sai
        print("pass")
    print("\n\n")
"""print_marks("sai",85,90,95)
print_marks("ram",96,90,84)
print_marks("shyam",45,10,20)
print_marks("karn",70,60,45)
print_marks("sam",78,90,95)"""

students=[("sai",85,90,95),
          ("ram",96,90,84),
          ("shyam",45,10,20),
          ("karn",70,60,45),
          ("sam",78,90,95)
          ]
for name,m1,m2,m3 in students:
    print_marks(name,m1,m2,m3)
