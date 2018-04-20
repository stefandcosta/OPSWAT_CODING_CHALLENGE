#!/usr/bin/python

import sys as sys
import requests as requests
import constant as constant


# GET THE FILE NAME
#filename = "sample_file.txt"
filename = sys.argv[1]

# GENERATE THE HASH FOR THE FILE
hashedFile = constant.hashEncoder(filename)

# API HIT TO CHECK FOR HASHED FILE
URL = constant.URL_HASH+hashedFile
REQUEST = requests.get(URL,headers = constant.HEADERS)
requestJson = REQUEST.json()

 
if(REQUEST.status_code == 200):
    #REQUEST FOR HASH FILE SUCCESSFUL....
    if(len(requestJson)==1):
        #HASHED FILE NOT FOUND !!
        URL = constant.URL_FILE
        REQUEST = requests.post(URL,headers=constant.HEADERS,files={'file':open(filename, 'rb')})
        requestJson = REQUEST.json()
        if(REQUEST.status_code == 200):
            #REQUEST FOR UPLOAD FILE SUCCESSFUL
            URL = constant.URL_FILE+requestJson['data_id']
            REQUEST = requests.get(URL,headers=constant.HEADERS)
            requestJson = REQUEST.json()
            if(REQUEST.status_code == 200):
                #UPLOADING FILE...
                while(requestJson['scan_results']['progress_percentage'] != 100):
                    URL = constant.URL_FILE+requestJson['data_id']
                    REQUEST = requests.get(URL,headers=constant.HEADERS)
                    requestJson = REQUEST.json()
                #UPLOAD COMPLETE !!
                constant.printJson(requestJson)
            
            else:
                #ERROR UPLOADING FILE...
                print("Error !!")
                print("Status Code:  "+REQUEST.status_code)
        else:
            #REQUEST FOR UPLOAD FILE UNSUCCESSFUL
            print("Error !!")
            print("Status Code:  "+REQUEST.status_code)
        
        
    else:
        #HASHED FILE FOUND
        constant.printJson(requestJson)
        
else:
    #REQUEST FOR HASH FILE UNSUCCESSFUL
    print("Error !!")
    print("Status Code:  "+REQUEST.status_code)