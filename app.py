import datetime
import sys
import re

def decode_timestamp(timestamp):

    #1/convert the timestamp to binary
    binary = bin(int(timestamp))[2:]

    #2/then take the first 41 binary characters and convert it to an integer.
    first41BinaryChars = binary[:41]

    #3/convert back from binary to an integer by passing in 2 as the base.
    timestamp = int(first41BinaryChars, 2)

    #4/convert the timestamp to milliseconds by dividing by 1000.
    return timestamp/1000 

def extract_timestamp():

    #get arguments passed in
    args = sys.argv[1:]
    url = args[0] if len(args) > 0 else None

    #our program expects a LinkedIn post url 
    if url is None:
        print("Error: No command line arguments provided. Please provide the link to the post.")
        sys.exit(1)
    elif "https" not in url:
        print(f"Error: Wrong Input: {url}. Please provide a full LinkedIn post url.")
        sys.exit(1)

    #extract the first argument
    postLink = args[0]

    #extract the encoded timestamp from the LinkedIn post url by using a regular expression.
    timestamp = re.search(r'[^-]\d+[^-]', postLink)
    
    #return the encoded timestamp value
    return None if timestamp is None else timestamp.group(0)
    
if __name__ == "__main__":
    
    #extract encoded timestamp from the LinkedIn post url
    encodedTimestamp = extract_timestamp()

   #print error if couldn't extract the timestamp
    if encodedTimestamp is None:
        print("Error: Could not extract timestamp. Make sure you pass in the full LinkedIn post url when executing this program.")
        sys.exit(1)

    #apply algorithm to extract the timestamp in iso format
    timestamp = decode_timestamp(encodedTimestamp)

    #format the timestamp to print nicely
    result = datetime.datetime.fromtimestamp(timestamp).isoformat()

    print("The timestamp is: " + str(timestamp) + " and the date is: " + str(result))
