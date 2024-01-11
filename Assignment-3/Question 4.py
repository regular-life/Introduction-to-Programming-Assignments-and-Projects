import time
class Course :
    
    def __init__(self,students,credits,assessments,policy):
        self.students=students
        self.credits=int(credits)
        self.assessments=assessments
        self.policy=policy
    
    def cutoff(self):
        cutoff=[]
        for j in range(len(self.policy)):
            lst=[]
            for i in self.students:
                if abs(self.policy[j]-i[1])<=2:
                    lst.append(i[1])
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
        return cutoff
    
    def grades(self):
        A=0
        B=0
        C=0
        D=0
        F=0 
        for i in self.students:
            if i[1]>=self.cutoff()[0]:
                A+=1
            elif self.cutoff()[0]>i[1]>=self.cutoff()[1]:
                B+=1
            elif self.cutoff()[1]>i[1]>=self.cutoff()[2]:
                C+=1
            elif self.cutoff()[2]>i[1]>=self.cutoff()[3]:
                D+=1
            else:
                F+=1
        print(f"Grading Summary : A - {A} , B - {B} , C - {C} , D - {D} , F - {F}")
        
    def getStudentdata(self):
        s=input("Type the student name : ")
        n=len(self.students)
        for i in range(n):
            if s==self.students[i][0]:
                ind=i
                break
        k=f'NAME : {s}\n'
        k+='MARKS : '
        for i in self.students[ind][2]:
            k+=i[0]
            k+=' - '
            k+=i[1]
            if i[0]!=self.assessments[-1][0]:
                k+=' , '
        k+=f"\nTOTAL MARKS : {self.students[ind][1]}\n"
        k+="GRADE : "
        if self.students[ind][1]>=self.cutoff()[0]:
            k+='A'
        elif self.cutoff()[0]>self.students[ind][1]>=self.cutoff()[1]:
            k+='B'
        elif self.cutoff()[1]>self.students[ind][1]>=self.cutoff()[2]:
            k+='C'
        elif self.cutoff()[2]>self.students[ind][1]>=self.cutoff()[3]:
            k+='D'
        else:
            k+='F'        
        print(f"\n\n{k}")
    
       
class Student :
    
    def __init__(self,marks):
        self.marks=marks
    
    def totalmarks(self):
        s=0
        for i in self.marks:
            s+=float(i[1])
        return s
   
cname, credits = map(str,input("Enter the course name and credits (with a space in between) ").split())
credits=int(credits)
# cname,credits="IP",4
s=0
assessments=[]
print('\n')
while s<100:
    method, weightage=map(str,input("Enter the assessment name and its' weightage (with a space in between) ").split())
    weightage=int(weightage)
    s+=weightage
    assessments.append((method,weightage))
# assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy=list(map(int,input("\nEnter the cutoff policy you would like to follow (with spaces in between) ").split()))
# policy = [80, 65, 50, 40]

n=int(input("\nEnter 1 if you wish to see the course summary. \nEnter 2 to view the grades of all students. \nEnter 3 to search for a student record.\n"))
s_t=time.time()
f=open('IP Assignment 3\Marks.txt','r')
f.seek(0,0)
t=f.readlines()
t=t[1:]
lst_students=[]
for i in t:
    name, labs, midsem, assignments, endsem=i.strip().split(',')
    am=name
    arr=[(f"{assessments[0][0]}" , labs) , (f"{assessments[1][0]}", midsem) , (f"{assessments[2][0]}", assignments) , (f"{assessments[3][0]}" , endsem)]
    name=Student(arr)
    total=name.totalmarks()
    lst_students.append((am,total,arr))

cn=cname
cname=Course(lst_students,credits,assessments,policy)

if n==1:
    print(f"Course Name : {cn}")
    print(f"Credits : {cname.credits}")
    print(f"Assessments : {cname.assessments}")
    print(f"Cutoffs : A - between {cname.cutoff()[0]} and {float(100)} ; B - between {cname.cutoff()[1]} and {cname.cutoff()[0]} ; C - between {cname.cutoff()[2]} and {cname.cutoff()[1]} ; D - between {cname.cutoff()[3]} and {cname.cutoff()[2]} ; F - below {cname.cutoff()[3]}")
    cname.grades()
elif n==2:
    z=open('IP Assignment 3\q5.txt','w')
    z.seek(0,0)
    for i in cname.students:
        sc=i[1]
        if sc>=cname.cutoff()[0]:
            grd='A'
        elif cname.cutoff()[0]>sc>=cname.cutoff()[1]:
            grd='B'
        elif cname.cutoff()[1]>sc>=cname.cutoff()[2]:
            grd='C'
        elif cname.cutoff()[2]>sc>=cname.cutoff()[3]:
            grd='D'
        else:
            grd='F'
        z.write(f"Name : {i[0]} , Total Marks : {i[1]} , Grade : {grd} \n")    
    z.close()
elif n==3:
    (cname.getStudentdata())
else:
    e_t=time.time()
    print(e_t-s_t)
    exit()
e_t=time.time()
print(e_t-s_t)