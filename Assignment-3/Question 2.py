f=open('IP Assignment 3\Q2.txt','r')
f.seek(0,0)
t=f.readlines()
t=t[1:]
def convert_to_seconds(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
t.sort(key = lambda x: convert_to_seconds(x[-9:-1]))
print("Press 1 if you wish to see student record and if the student is present in the campus or not ")
print("Press 2 if you wish to see all entry/exit records in a given time frame ")
print("Press 3 if you wish to see the number of times students have entered and exited from a given gate ")
n=int(input())
if n==1:
    z=open('IP Assignment 3\q2(1).txt','w')
    z.seek(0,0)
    student_name=input("Enter student name ")
    crnt_time=input("Enter current time ")
    cu_hr,cu_min,cu_ss=crnt_time.split(':')
    d={}
    d[student_name]=[]
    for i in t:
        time=i[-9:-1]
        a_hr,a_min,a_ss=time.split(':')
        if cu_hr>a_hr:
            name,status,gate_no,p=i.strip().split(',')
            if name==student_name:
                d[student_name].append((status, gate_no,p))
        elif cu_hr==a_hr:
            if cu_min>a_min:
                name,status,gate_no,p=i.strip().split(',')
                if name==student_name:
                    d[student_name].append((status, gate_no,p))      
            elif cu_min==a_min:
                if cu_ss>=a_ss:
                    name,status,gate_no,p=i.strip().split(',')
                    if name==student_name:
                        d[student_name].append((status, gate_no,p))
                else:
                    break
            else:
                break
        else:
            break
    status=d[student_name][-1][0]
    status=status[1:len(status)]
    print(f"{student_name} last {status.lower()}ed the campus.",end=" ")
    if status=="ENTER":
        print(f"{student_name} is inside the campus.")
    else:
        print(f"{student_name} is outside the campus.")
    z.write(student_name)
    z.write('\n')
    for i in d[student_name]:
        z.write(str(i))
        z.write('\n')
    z.close()
elif n==2:
    start_hr,start_min,start_ss=input("Enter the starting time in 24-hr format. ").split(':')
    end_hr,end_min,end_ss=input("Enter the ending time in 24-hr format. ").split(':')
    z=open('IP Assignment 3\q2(2).txt','w')
    for i in t:
        time=i[-9:-1]
        a_hr,a_min,a_ss=time.split(':')
        if start_hr<a_hr:
            if a_hr<end_hr:
                z.write(i)
            elif a_hr==end_hr:
                if a_min<end_min:
                    z.write(i)
                elif a_min==end_min:
                    if a_ss<end_ss:
                        z.write(i)
                    elif a_ss==end_ss:
                        z.write(i)
        elif start_hr==a_hr:
            if a_min>start_min:
                z.write(i)
            elif a_min==start_min:
                if a_ss>start_ss:
                    z.write(i)  
                elif a_ss==start_ss:
                    z.write(i)
    z.close()
elif n==3:
    gn=int(input("Please enter the gate number "))
    en=0
    ex=0
    for i in t:
        name,status,gate_no,time=i.strip().split(',')
        if gate_no==f" {gn}":
            if status==' ENTER':
                en+=1
            else:
                ex+=1
    print(f"Number of times people entered through this gate is {en}.")
    print(f"Number of times people exited through this gate is {ex}.")
else:
    exit()
f.close()