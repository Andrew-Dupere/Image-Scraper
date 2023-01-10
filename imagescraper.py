import bs4
import requests
import os

#Create a new folder to store the images
def createfolder(images):
    try:
        folder = input('Folder Name: ')
        os.mkdir(folder)
        
    except:
        print('Folder Already Exists')
        createfolder()
        
    #run download function after folder has been created
    
    download(images,folder)
        
def download(images,folder):

    #create a counter to keep track of how many images are found
    
    counter = 0
    print(f'{len(images)} images found')
    
    #make sure images exist on the webpage
    
    if len(images) != 0:
        
#A series of try and except blocks to iterate through potential image tags in the HTML code
        
    
        for i, image in enumerate(images):
            
            try:
                link = image['data-srcset']
                
            except:
                try:
                    link = image['data-src']
                    
                except:
                    try: 
                        link = image['data-fallback-src']
                    
                    except:
                        try:
                            link = image['src']
                            
                        except:
                            pass
                        
            #use requests to extract the HTML code
            
            try:
                r = requests.get(link).content
                
                #set an encoding paramter if needed
                
                try:
                    r = str(r, 'utf-8')
                
                except UnicodeDecodeError:
                    
                    #iniatiate download
                    
                    with open(f'{folder}/images{i+1}.jpg','wb+') as f:
                        f.write(r)
                    counter += 1
                    
            except:
                pass
                
        #Notify user that download is complete    
        
        if counter == len(images):
            print('Image Download Complete')
            
        #Notify user if only a partial download was possible
        
        else:
            print(f'{counter} Images out of {len(images)} Dwonloaded')
            
#Define the Primary Function          

def primary(site):

    #request HTML code from site
    
    r = requests.get(site)
    
    #create soup and parse HTML code
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #find all images in the soup we created
    
    images = soup.findAll('img')
    
    #call folder create function after variables are defined
    #the create folder function will run the download function after folder creation is complete
    
    createfolder(images)
    
#Ask user for a url and then run the primary function

site = input('Which site would you like to scrape? ')
        
primary(site)
