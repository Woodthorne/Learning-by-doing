import os, csv

data = [['File name','Word count']]

if not os.path.exists('file_analysis.csv'):
    with open('file_analysis.csv','x'):
        pass

def main():
    recon()
    with open('file_analysis.csv','w',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def recon(checkFolder=os.getcwd()):
    returnFolder = os.getcwd()
    os.chdir(checkFolder)
    current_content = os.listdir()
    for item in current_content:
        if item[-4:] == '.txt':
            analyse_txt(item)
        elif '.' not in item:
            nextFolder = checkFolder + f'\{item}'
            recon(nextFolder)
    os.chdir(returnFolder)

def analyse_txt(filename):
    global data
    wordcount = 0
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            wordcount += len(line.split(' '))
    data.append([filename, wordcount])

if __name__ == '__main__':
    main()