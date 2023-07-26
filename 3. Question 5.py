import time
cname, credits = map(str,input("Enter the course name and credits (with a space in between) ").split())
credits=int(credits)
# cname,credits="IP",4
s=0
assessments=[]
while s<100:
    method, weightage=map(str,input("\nEnter the assessment name and its' weightage (with a space in between) ").split())
    weightage=int(weightage)
    s+=weightage
    assessments.append((method,weightage))
# assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy=list(map(int,input("\nEnter the cutoff policy you would like to follow (with spaces in between) ").split()))
# policy = [80, 65, 50, 40]
f=open('IP Assignment 3\Marks.txt','r')
f.seek(0,0)
t=f.readlines()
t=t[1:]

print("\n\nPress 1 if you wish to view the course summary. ")
print("Press 2 if you wish to print grades of all the students in a file. ")
print("Press 3 if you wish to search for a student record. ")

d={}
t_stu={}
for i in t:
    name, labs, midsem, assignments, endsem=i.strip().split(',')
    d[name]=[float(labs),float(midsem),float(assignments),float(endsem)]
    t_stu[name]=float(labs)+float(midsem)+float(assignments)+float(endsem)
cutoff=[]
for j in range(len(policy)):
    lst=[]
    for i in t_stu.values():
        if abs(policy[j]-i)<=2:
            lst.append(i)
    if len(lst)>1:
        lst.sort()
        diff=0
        for i in range(len(lst)-1):
            if abs(lst[i+1]-lst[i])>diff:
                diff=lst[i+1]-lst[i]
                x,y=lst[i+1],lst[i]
        cutoff.append(float((x+y)/2))
    else:
        try:
            cutoff.append(float(lst[0]))
        except IndexError:
            cutoff.append(policy[j])
n=int(input())
s_t=time.time()
if n==1:
    print(f"Course Name : {cname} \nCourse Credits : {credits}")
    k='Assessments : '
    for i in range(len(assessments)):
        k+=assessments[i][0]
        k+=' , '
        k+=str(assessments[i][1])
        if i!=len(assessments)-1:
            k+=' ; '
    print(k)
    A=0
    B=0
    C=0
    D=0
    F=0
    print(f"Cutoffs : A - between {cutoff[0]} and {float(100)} ; B - between {cutoff[1]} and {cutoff[0]} ; C - between {cutoff[2]} and {cutoff[1]} ; D - between {cutoff[3]} and {cutoff[2]} ; F - below {cutoff[3]}")
    for i in t_stu.values():
        if i>=cutoff[0]:
            A+=1
        elif cutoff[0]>i>=cutoff[1]:
            B+=1
        elif cutoff[1]>i>=cutoff[2]:
            C+=1
        elif cutoff[2]>i>=cutoff[3]:
            D+=1
        else:
            F+=1
    print(f"Grading Summary : A - {A} , B - {B} , C - {C} , D - {D} , F - {F}")
elif n==2:
    z=open('IP Assignment 3\q5.txt','w')
    z.seek(0,0)
    for i in t_stu.keys():
        sc=t_stu[i]
        if sc>=cutoff[0]:
            grd='A'
        elif cutoff[0]>sc>=cutoff[1]:
            grd='B'
        elif cutoff[1]>sc>=cutoff[2]:
            grd='C'
        elif cutoff[2]>sc>=cutoff[3]:
            grd='D'
        else:
            grd='F'
        z.write(f"Name : {i} , Total Marks : {t_stu[i]} , Grade : {grd} \n")    
    z.close()
elif n==3:
    s=input("Type the student name : ")
    s_t=time.time()
    k='MARKS : '
    for i in range(len(assessments)):
        k+=assessments[i][0]
        k+=' - '
        k+=str(d[s][i])
        if i!=len(assessments)-1:
            k+=' , '
    k+=f"\nTOTAL MARKS : {t_stu[s]}\n"
    sc=t_stu[s]
    if sc>=cutoff[0]:
        grd='A'
    elif cutoff[0]>sc>=cutoff[1]:
        grd='B'
    elif cutoff[1]>sc>=cutoff[2]:
        grd='C'
    elif cutoff[2]>sc>=cutoff[3]:
        grd='D'
    else:
        grd='F'
    k+=f"GRADE : {grd}" 
    print(k)
e_t=time.time()
print(e_t-s_t)