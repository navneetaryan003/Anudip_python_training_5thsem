def open_file(filename , mode):
    #opening the file
    try:

        #returning the file
        return open(filename , mode)
    
    #handling the file not found error
    except FileNotFoundError:
        print("File not found")
        return None