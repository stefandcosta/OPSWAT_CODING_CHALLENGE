import hashlib as hash

# IMPORTANT CONSTANT DATA DECLARATIONS

API_KEY = ""            #ADD API KEY HERE
URL_HASH = "https://api.metadefender.com/v2/hash/"
URL_FILE = "https://api.metadefender.com/v2/file/"
BUFFER_SIZE = 65536
HEADERS = {'apikey':API_KEY}


# CREATE HASH OF THE FILE USING MD5 
def hashEncoder(file):
    hashedFile = hash.md5()
    with open(file, 'rb') as f:
        while True:
            buffer = f.read(BUFFER_SIZE)
            if not buffer:
                break
            hashedFile.update(buffer)
    return hashedFile.hexdigest()


# PRINT THE RESULT JSON
def printJson(json):
    print("filename:"+json['file_info']['display_name'])
    print("overall_status:"+json['scan_results']['scan_all_result_a'])
    print("")
    for key, value in json['scan_results']['scan_details'].items():
        print("engine: "+str(key))
        if(value['threat_found']==""):
            print("threat_found: Clean")
        else:
            print("threat_found: "+ str(value['threat_found']))
        print("scan_result: "+str(value['scan_result_i']))
        print("def_time: "+str(value['def_time']))
        print("")
