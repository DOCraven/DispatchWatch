#libraries

import pandas as pd
import datetime
import os 
import requests
import zipfile 
import shutil

from datetime import datetime
from bs4 import BeautifulSoup
from os import walk
from zipfile import ZipFile





#### NOTES


##################
#                #
#                #
#     V0.1.0     #
#                #
#                #
##################

### PSEUDOCODE ####
#scrape entire archive
#download last [-1] csv
#extract said csv
#import as pd
#manipulate data
    #include time code was run
#save as csv, stomping over last csv
#run script at xx05h and xx35h




#### FUNCTIONS ####

def PathChecker(): 
    """checks to see if output DIRS are created, if not, creates them"""
    cwd = os.getcwd()
    
    DL_PATH = cwd + '\\DL'
    if not os.path.exists(DL_PATH): #make DL folder if it does not exist
        os.makedirs(DL_PATH)

    
    return #nothing

def deleter(folder):
    """
    Emptys the folder specified
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))    
    
def fileScanner(path): 
    """ 
    this will scan all files in the root dir, subfolders, and return a list of file names
    """
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    return f

def downloader(): 
    """ downloads last ZIPFILE in given URL"""
    
    ## 
    
    ### STEP 1 set up the env
    cwd = os.getcwd()#get current dir
    download_folder = cwd + "\\DL" 
    root = 'http://nemweb.com.au/' #ENTER THE ROOT OF THE WHOLE DIR (ie, just to the TLD)
    URL = "http://nemweb.com.au/Reports/Current/PredispatchIS_Reports/"

    if not os.path.exists(download_folder): #make DL folder if it does not exist
        os.makedirs(download_folder)
    
    ### STEP 2 - Scrape for URLS 
    r = requests.get(URL) 
    soup = BeautifulSoup(r.text, 'lxml')
    
    all_hrefs = soup.find_all('a')
    all_links = [link.get('href') for link in all_hrefs]
    zip_files = [dl for dl in all_links if dl and '.zip' in dl]

    ### STEP 3 - Download last ZIP file 
    zip_file = zip_files[-1] #get last zip file
    full_url = root + zip_file #concat the full url
    r = requests.get(full_url)
    zip_filename = os.path.basename(zip_file)
    dl_path = os.path.join(download_folder, zip_filename)
    with open(dl_path, 'wb') as z_file:
        z_file.write(r.content)



    return #nothin 



















#### MAIN #####

def DispatchWatch():
    """ Main function"""

    ### STEP 1 - set up the env
    ## VARS
    
    cwd = os.getcwd() #get current working dir
    DL = cwd + '\\DL'
    deleter(DL)
    ### STEP 2 - download data
    downloader() #download most recent upload from NEMWEB

    ### STEP 3 - unzip data, load into memory as csv
    # Zipper()
    
    ### STEP 4 - modify pd (will be the hard one)
    # Organiser()
    
    

    return #nothing 



    ### MAIN


DispatchWatch()

print("CODE COMPLETED")