#Elzinus found this script at <https://atcoordinates.info/tag/zim-wiki/>
#And modified it for Markdown use
#Created original by: Frank Donnelly’s 

#Parse notes stored in zim wiki to extract all bibtex records and write them
#to a new bibtex file named under value 'outfile'.
 
# === FILEFORMAT ===
#Script must be stored directly above the notes folder where the data files
#are stored. It will ignore the empty bibtex template files and will only
#read wiki files stored as .markdown. (if you use other formats change both
#instances of .mardown).

# === TAGING OF BIB INFORMATION IN YOUR FILES ===
#The script reads each line and ignores them until it finds the open
#tag. Then it starts writing each line until it reads the close  tag.
#A line return is appended so records are separated in the output file.

#Within the markdown document, all bibtex records in the notes you want to in-
#clude need to be enclosed in a bibtex TAG. In this script I use '<bibtex> 
#but you can change this easy according to your whishes.


#A list and count of extracted records is provided as a diagnostic

import os, datetime
 
now=datetime.date.today()
path='.'
#Change outfile if you want to use another name for your .bib file
#outfile='sources_'+str(now)+'.bib'
outfile='bibref.bib'

writefile=open(outfile,'w')
 
counter=0
titles=[]
 
for (subdir,dirs,files) in os.walk(path):
    if 'Templates' in dirs:
        dirs.remove('Templates')
    if 'documents' in dirs:
        dirs.remove('documents')
    for file in files:
        if file[-9:]=='.markdown':
            readfile=open(os.path.join(subdir,file),'r')
            for line in readfile:
# Change <bibtex> if you use another opening tag in your files
                if line.startswith('<bibtex>'):
                    break
            for line in readfile:
# Here you can change the end tag if you use differently
                if line.startswith('</bibtex>'):
                    titles.append(file)
                    writefile.write('\n')
                    counter=counter+1
                    break
                else:
                    writefile.write(line)
            readfile.close()
writefile.close()
 
titles = [t.replace('_', ' ') for t in titles]
titles=[t.strip('.markdown') for t in titles]
titles.sort()
print('Bibliographic records have been extracted for the following sources:','\n')
for title in titles:
    print('*',title)
print('\n')
print(counter,'bibilographic records have been parsed and written to',outfile)
