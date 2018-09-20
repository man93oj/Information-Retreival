'''
Course: Information Retrieval
Homework 1: Text processing

MANOJ PRABHAKAR NALLABOTHULA
UIN: 662749754

'''
import os

def GetFilesList(dirName):
    # create a list of file and subdirectories names
    FilesList = os.listdir(dirName)
    AllFilesList = []
    for entry in FilesList:
        # Create a full file path
        FullFilePath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(FullFilePath):
            AllFilesList = AllFilesList + GetFilesList(FullFilePath)
        else:
            AllFilesList.append(FullFilePath)
    return AllFilesList
    
def ReadFile(FileName):
    with open(FileName,'r') as f:
        t = f.read()
        return t
        
def main():
    usage = '''
            Please give two arguments for this script
            eg: Python IR_FirstAssignment.py Citeseer 1
            where "Citeseer" is the folder name
                  "0" NOT to Integrate Porter stemmer and a stopword eliminator
                  "1" to Integrate Porter stemmer and a stopword eliminator  
    	    '''
    # importing sys for arguments
    import sys
    if (len(sys.argv) <> 3):
        print usage
        sys.exit()
        
    dirName = sys.argv[1]
    
    ProcessedList = []
    if os.path.isfile (dirName):
       FileText = ReadFile (dirName)
       if sys.argv[2] == '0':
	  from PreProcessor import Preprocessing
          ProcessedList = Preprocessing(FileText)
       elif sys.argv[2] == '1':
          from PreProcessor import Porter
          ProcessedList = Porter(FileText)
    else:
       # get the list of files in a directory
       FilesList = GetFilesList (dirName)
       FilesText = []
       # read file contents
       for File in FilesList:
           text = ReadFile (File)
           FilesText.append (text)
       if sys.argv[2] == '0':
          from PreProcessor import Preprocessing
          ProcessedList = Preprocessing(FilesText)
       elif sys.argv[2] == '1':
          from PreProcessor import Porter
          ProcessedList = Porter(FilesText)
 
    
    # 2A total number of words in a collection
    striped_length = len(ProcessedList)
    print('2A answer: {0}'.format(striped_length))
    
    # 2B unique list length
    from collections import Counter
    cnt = Counter(ProcessedList)
    print('2B answer: {0}'.format(len(list(cnt))))

    # 2C top 20 high frequency words
    print('2C answer: {0}'.format(cnt.most_common(20)))

    # 2D number of stopwords
    from PreProcessor import GetStopWordsList
    StopwordList = GetStopWordsList()
    swCount = 0
    print("2D answer: ")
    for x,y in cnt.most_common(20):
    	if x in StopwordList:
            swCount += 1
            print('{0}'.format(x))
    print('There are {0} Stopwords in Top 20 high frequency words.'.format(swCount))
    
    # 2E greater than 15% of total words
    total = 0
    account = 1
    stripe_lenght = (int)(0.15*striped_length)
    for x,y in cnt.most_common():
    	total += y
        if (total >= stripe_lenght):
            break
    	else:
    	    account += 1
    print('2E answer: {0}'.format(account))
           
if __name__ == '__main__':
    main()
