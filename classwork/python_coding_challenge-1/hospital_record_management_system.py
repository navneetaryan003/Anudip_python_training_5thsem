#  Hospital Patient Record Management System
# Problem Statement
# A hospital maintains patient details in a file named patients.txt.
# Sample Input/Data (patients.txt)
# P101,Anuj,Normal
# P102,Rahul,Critical
# P103,Priya,Stable
# P104,Neha,Critical
# P105,Amit,Stable
# P106,Sneha,Normal
# P107,Karan,Critical
# P108,Pooja,Stable
# P109,Rohit,Normal
# P110,Anjali,Stable
# Tasks
# 1. Display all patient records.
# 2. Display critical patients.
# 3. Count patients under each status.
# 4. Search patient details using Patient ID.
# 5. Save critical patient records to critical_patients.txt.


file=open("classwork/python_coding_challenge-1/patients.txt","r")

if not file:
    exit("file is not opened")


    

#1.display all patient records
print("All patient records:")    
for line in file:
    data=line.strip().split(",")
    print("Patient ID:",data[0])
    print("Name:",data[1])
    print("Status:",data[2])
    print()


#2.display critical patients

file.seek(0)
print("Critical patients:")

for line in file:

    #splitting the data
    data=line.strip().split(",")
    if data[2]=="Critical":
        print(data[1])
        


#3.count patients under each status
file.seek(0)
print("Count of patients under each status:")

count_normal=0    #count of normal patients
count_critical=0   #count of critical patients
count_stable=0     #count of stable patients

for line in file:

    #splitting the data
    data=line.strip().split(",")

    if data[2]=="Normal":
        count_normal+=1
    elif data[2]=="Critical":
        count_critical+=1
    elif data[2]=="Stable":
        count_stable+=1

print("Normal:",count_normal)
print("Stable:",count_stable)
print("Critical:",count_critical)


#4.search patient details using Patient ID
file.seek(0)
patient_id=input("Enter the patient ID to be searched: ")

#validate patient ID
if not patient_id.replace(" ","").isalnum():
    print("Invalid patient ID. Please enter a valid ID.")
    exit()

for line in file:

    #splitting the data
    data=line.strip().split(",")

    if data[0]==patient_id:
        print("patient found :")
        print("Patient ID:",data[0])
        print("Name:",data[1])
        print("Status:",data[2])
        print()
        break
else:
    print("Patient not found.")


#5.save critical patient records to critical_patients.txt
file.seek(0)
critical_patients_file=open("classwork/python_coding_challenge-1/critical_patients.txt","w")

for line in file:

    #splitting the data
    data=line.strip().split(",")

    #writing the data
    if data[2]=="Critical":
        critical_patients_file.write(line)
      

print("Critical patient report generated successfully.")

#closing the crictical patients file
critical_patients_file.close()

#closing the patients file
file.close()
