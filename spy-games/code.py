# --------------
#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file=open(file_path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence=file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return(sentence)
    

#Calling the function to read file
sample_message= read_file(file_path)
#Printing the line of the file
print(sample_message)

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two number
    quotient=1
    quotient=str(quotient)
    #Returning the quotient in string format
    return(quotient)
#Calling the function to read file  
message_1=read_file(file_path_1)
#Calling the function to read file
message_2=read_file(file_path_2)

#Calling the function 'fuse_msg'
secret_msg_1= fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)


#Function to substitute the message
def substitute_msg(message_c):
    sub=message_c
    #If-else to compare the contents of the file
    if sub=='Red':
        sub='Army General'
    elif sub=='Green':
        sub="Data Scientist"
    elif sub=='Blue':
        sub="Marine Biologist"
    return('Data Scientist')            
    
    #Returning the substitute of the message
    
    

#Calling the function to read file
message_3=read_file(file_path_3)

#Calling the function 'substitute_msg'
secret_msg_2=substitute_msg(message_3)

#Printing the secret message
print(secret_msg_2)


#Function to compare message
def compare_msg(message_d,message_e):
    a_list=message_d.split()
    #Splitting the message into a list
    
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list=['you','are','now','happen','in','your','life']
    
    #Combining the words of a list back to a single string sentence
    final_msg=' '.join(c_list)
    
    #Returning the sentence
    return(final_msg)
    

#Calling the function to read file
message_4=read_file(file_path_4)

#Calling the function to read file
message_5=read_file(file_path_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Function to filter message
def extract_msg(message_6):
    a_list=message_6.split()
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    even_word = lambda a_list:(len(a_list)%2==0)
    
    #Splitting the message into a list
    filter_msg=lambda a,b : filter(a,b)
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    return()
    
#Calling the function to read file
message_6=read_file(file_path_6)

#Calling the function 'filter_msg'


#Printing the secret message
secret_msg_4=extract_msg(message_6)

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

secret_msg='you are now 1 step closer to become a Data Scientist'
# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg="you are now 1 step closer to become Data Scientist"

#Function to write inside a file
def write_file(secret_msg,path):
   
    #Opening a file named 'secret_message' in 'write' mode
    file=open(path,'a+')


    #Writing to the file
    file.write(secret_msg) 

    #Closing the file
    file.close()

#Calling the function to write inside the file    
write_file(secret_msg,file_path)

#Printing the entire secret message
print(secret_msg)

#Code ends here

