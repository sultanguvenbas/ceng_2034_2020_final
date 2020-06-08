#!/usr/bin/python3
import os,requests,sys,uuid,hashlib
#SULTAN GUVENBAS

url = ["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

array=[] #create new array
def download_file(url, filename=None):
    r=requests.get(url, allow_redirects=True)
    file = filename if filename else str(uuid.uuid4())
    file="downloads/"+file  #ı create new folder and download here
    open(file, 'wb').write(r.content)
    hasher=hashlib.md5()
    hasher.update(r.content)
    digest=hasher.hexdigest()
    if digest in array:
    	print("This is duplicate: "+url)
    	print('-'*80) #used it to separate the results
    	print()
    else:
    	array.append(digest)
    
    



print("I am ",os.getpid())
print('-'*50) #used it to separate the results

def parent_child(): 

    child = os.fork() 
    
    # child greater than 0  means parent process 
    if child > 0:
        os.waitpid(child, 0) #waiting child processor
        print("Parent process and id is : ", os.getpid()) 
        print('-'*50) #used it to separate the results
        
  
    # child equals to 0 means child process 
    elif(child == 0): 
        print("Child process and id is : ", os.getpid()) 
        print('-'*20 + "parent is waiting"+"-"*20) #used it to separate the results
        
        for i in range (len(url)):
            download_file(url[i])   #"imagei{}".format(i+1))
            
            
         #os._exit(0)
    #if child is less than 0
    else:
        print("Error !!!")
  

       
# Driver code 
parent_child() 






 
   




