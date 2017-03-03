
import urllib

def read_text():
    counter=0;
    with open("/home/sudeep/Udacity - Programming foundations with python/Profanity_editor/movie_quotes.txt") as fp:
        for line in fp:
            output = profanity_check(line)        
            if output is "true":
                print("Cuss word found in line:"+line)
                counter=counter+1
        if(counter==0):
            print("File has been proof-read. No cuss words found! Congratulations!")
    
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

        
