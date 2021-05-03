from time import gmtime, strftime

def journal():
    content = ""
    infile = open("account.txt", "w")
    infile.write(str(strftime("%a, %d %b %Y %H:%M:%S +0000 \n", gmtime()) + ' '))
    print("Input text: ", end='')
    while 1:
        content = input()
        infile.write("\n")
        if content == "exit":
            break
        infile.write(content)




    infile.close()


journal()
