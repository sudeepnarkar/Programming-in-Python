
import urllib

def read_text():
    counter=0;
    with open("file-path") as fp:
        for line in fp:
            output = profanity_check(line)        
            if output is "true":
                print("Curse word found in line:"+line)
                counter=counter+1
        if(counter==0):
            print("File has been proof-read. No curse words found! Congratulations!")
    
    #file_content=file.read()
    #print(file_content)
    
    
    

def profanity_check(content_to_check):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+content_to_check)
    response = conn.read()
    if "true" in response:
        return ("true")
    else:
        return("false")

read_text()    

        
