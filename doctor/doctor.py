
"""
Mehmet Oğuzhan TOR
21301554
20/12/2020
CS 115 - 2
"""

class Doctor:
    
    def __init__(self, dId, dName, dSpec, hosp):
        self.__doctorId = dId
        self.__doctorName = dName
        self.__specialty = dSpec
        self.__hospital = hosp

    def get_doctor_id(self):
        return self.__doctorId
    
    def set_doctor_id(self, dId):
        self.__doctorId = dId

    def get_doctor_name(self):
        return self.__doctorName

    def set_doctor_name(self, dName):
        self.__doctorName = dName
    
    def get_specialty(self):
        return self.__specialty
    
    def set_specialty(self, dSpec):
        self.__specialty = dSpec

    def get_hospital(self):
        return self.__hospital

    def set_hospital(self, hosp):
        self.__hospital= hosp
    
    def __repr__(self):
        return self.__doctorId+' '+self.__doctorName+' '+self.__specialty+' '+self.__hospital
    
    def __lt__(self,other):
        return self.__doctorId < other.__doctorId
    
           
def bubble_sort(doc_list):
    '''
    : takes a list of Doctors as a parameter, and sorts the doctors according to their
    hospital name and specialty. The list should be sorted in place, no new lists should be created.

    Parameters
    ----------
    doc_list : list that includes the doctors
        

    Returns
    -------
    The function sorts the doctors in the list by using a nested loop.

    '''
    #lenght of the doc_list list
    lenght=len(doc_list);
    
    for i in range(lenght-1):
        for j in range(i+1,lenght):
          
            if (doc_list[i].get_specialty()>doc_list[j].get_specialty()) and doc_list[i].get_hospital()==doc_list[j].get_hospital():
                t=doc_list[i];
                doc_list[i]=doc_list[j];
                doc_list[j]=t;
            elif doc_list[j].get_hospital() < doc_list[i].get_hospital():
                t=doc_list[i];
                doc_list[i]=doc_list[j];
                doc_list[j]=t;
    
def binary_search(doc_list,doc_ID):
    '''
     a recursive function that takes a list of Doctors, the id of a doctor to search
     and the starting and ending index of the list to be searched as parameters. The function should
     return the index of the doctor with the given id or -1 if the doctor does not exist in the list.
   
    Parameters: doc_list : is the list of doctors
    doc_ID the ID that is being searched
    length is the len of the doc_list
    
    returns if the ID is in the list and its place in the list
    and returns None if the ID is not in the list
    '''
    lenght = len(doc_list)
    low = 0
    
    # an endless while loop that ends when it finds the doc_ID or it is not in the list
    n = 2
    while n < 3:
        if (lenght-1) >= low:
            middle = (lenght-1 + low)//2
            if doc_list[middle].get_doctor_id() == doc_ID:
                break
            elif doc_list[middle].get_doctor_id() > doc_ID:
                lenght = middle 
            else: 
                low = middle +1
        else:
            middle = -1 
            break
    if (middle == -1):
        return None
    else:
        return doc_list[middle]

def read_doctors(file):
    '''
    takes a file name as parameter, and using the file data, creates a list of Doctor
    objects from the data in the input file and returns the Doctor list.

    Parameters
    ----------
    file : file is the text file where all of the information is in.

    Returns
    -------
    file_list : a list that contains the information in a list format

    '''
    read_file = open(file, 'r')
    file_list = []
    for line in read_file:
        the_line = line.rstrip("\n").split(';')
        doc_ID = the_line[0]
        doc_name = the_line[1]
        doc_spec = the_line[2]
        doc_hosp = the_line[3]
        file_list.append(Doctor(doc_ID, doc_name, doc_spec, doc_hosp))
    return file_list

#The file that should be read
docs = read_doctors('doctors.txt')

# sorting the file
docs.sort()

# Asking for an ID of doctor to search from the user
input_ID = input ("Enter id of doctor to search: ")

#using the binary_search function to find the ID in the list
the_doc = binary_search(docs, input_ID)

#Printing the information that is gotten from the functions
if(the_doc == None):
    print("No such doctor")
else:
    print("Doctor with id %s"%the_doc.get_doctor_id())
    print(the_doc)
    
#using bubble_sort function
bubble_sort(docs)

#Printing the doctors by hospital and speciality
print("Doctors by Hospital and Speciality:")
for doc in docs:
    print(doc)
          
          
          
          


        
            
            
            
