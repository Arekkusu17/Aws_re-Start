import re

insulinFile=open("preproinsulin-seq.txt","r")
#cleanInsulinFile=open("preproinsulin-seq-clean.txt","a")
count=0

txt=insulinFile.read()
cleanTxt="".join(re.findall("[a-z]", txt))

#cleanInsulinFile.write(str(cleanTxt))
#cleanInsulinFile.close()

print("Clean file written.")


for i in range(0,110):
    if i>88:
        aInsulinSeqCleanFile=open("ainsulin-seq-clean.txt","a")
        print(i)
        aInsulinSeqCleanFile.write(cleanTxt[i])
    if 89>i>53:
        cInsulinSeqCleanFile=open("cinsulin-seq-clean.txt","a")
        print(i)
        cInsulinSeqCleanFile.write(cleanTxt[i])
    if 54>i>23:
        bInsulinSeqCleanFile=open("binsulin-seq-clean.txt","a")
        print(i)
        bInsulinSeqCleanFile.write(cleanTxt[i])
    elif i<24:
        isInsulinSeqCleanFile=open("Isinisulin-seq-clean.txt","a")
        print(i)
        isInsulinSeqCleanFile.write(cleanTxt[i])
        






"""
with open ("preproinsulin-seq.txt","r") as input:
    
    with open("preproinsulin-seq-clean.txt","a") as outfile:
        
        for line in input:
            txt+=line
        cleanTxt = re.findall("[a-z]", txt)
        outfile.write("".join(cleanTxt))
        
print (cleanTxt)

"""