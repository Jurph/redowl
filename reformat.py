# Converts a wordlist from:
# "aglet","algae","anvil" format 
# to: 
# aglet
# algae
# aglet 
# ...in case you ever have to extract such a wordlist
# from a website's javascript or HTML 

filename = "commas.txt"
outfile = "lines.txt"
wordbank = [line.rstrip() for line in open(filename)]
with open(outfile, 'a') as out:
    for j in wordbank:
        print("This next string is {} characters long.".format(len(j)))
        k = j.replace(',','\n')
        l = k.replace('"', '')
        out.write(l)