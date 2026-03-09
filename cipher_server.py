import time
import zmq 


#set up communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

def process_message(message, key):
    shift = key % 26

    new_message = ""

    #visit each character
    for char in message:

        #check if char is a space
        if char == " ":
            new_message += " "
            continue

        #get ascii value
        char = ord(char) 

        #get new ascii value
        new_ascii_char = (char + shift)

       #wrap around alpabet
        if new_ascii_char > 122:
            new_ascii_char = (new_ascii_char % 122) + 96
        elif new_ascii_char < 97:
            new_ascii_char = 122 - (97 - new_ascii_char)
        new_char = chr(new_ascii_char)
        new_message += new_char

    return new_message

#loop for communication
while True:
    #get communication
    pre_message = socket.recv()
    socket.send_string("Ready for Key")
    message = str(pre_message.decode())
    message = message.lower()

    time.sleep(.5)
    pre_key = socket.recv()
    socket.send_string("Ready for mode")
    key = int(pre_key.decode())

    time.sleep(.5)
    pre_mode = socket.recv()
    mode = str(pre_mode.decode())


    #Get 
    if len(message) > 0 and key is not None and len(mode) > 0:
        #quit on Q
        if message == 'Q' or mode == 'Q': 
            break
        
        #encypt message
        elif mode == "e":
            processed_message = process_message(message, key)
            

        #decrypt the message
        elif mode == "d":
            processed_message = process_message(message, -(key))
            
        else:
            processed_message = "An error occured"

        socket.send_string(processed_message)
        

#end communication
context.destroy()
