from sys import argv            # Import module

script, filename = argv             #get varaibles from user

print "We're going to erase %r." % filename         #print alert about erase file.
print "If you don't want that hit CTRL-C (^C)."     #click CTRL+C to cancle
print "If you want that, hit RETURN."               #press ENTR to continue

raw_input("?")          #ask what to do.

print "Opening the file ..."
target = open(filename, 'w')            #open file for writing

print "Truncating the file ..."         
target.truncate()               #reasing the file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to file."

target.write(line1)     #Insert line 1
target.write("\n")      #open new line
target.write(line2)     #Insert line 2
target.write("\n")      #open new line
target.write(line3)     #Insert line 3
target.write("\n")      #open new line

print "Ande finally, we close it."
target.close()          #close the file


