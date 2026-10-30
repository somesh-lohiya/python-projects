# Create a program that Sstores student names and marks in a text file and allows the user to view the stored records.

def st():
    with open('stored_names', 'a+') as f:
        while True:
            n = input("Enter the student's name: ")
            
            f.seek(0)
            data = f.read()
            
            if n in data:
                p = input("Entered name already exists in file, Do you want to remain the name same or renter: ")
                if p == 'renter':
                    continue
            
            m = input("Enter marks: ")
            
            f.write(f"{n} : {m}\n")
            print("Name entered successfully:")
            
            p1 = input("Do you want to enter more names(y/n): ")
            if p1 == 'y':
                continue
            else:
                break

def view():
    with open('stored_names', 'r') as f:
        c = 1               
        while True:
            line = f.readline()
            if not line:      
                break
            print(c, line.strip())
            c += 1            

st()
view()