HEADER_LEN = 10

msg = "SFAFFSAFAFAGDBYEDUDEHELLODUDEFAfwfwgwgwggwgwegewgew"
packet = "HELLODUDE" + msg + "GDBYEDUDE"
message = packet
print(message)
while True:
    if (message.find("GDBYEDUDE")) == -1:
        break
    i = message.find('HELLODUDE')
    j = message.find("GDBYEDUDE")
    print(message[i + HEADER_LEN:j])
    message = message[j + HEADER_LEN:]
    