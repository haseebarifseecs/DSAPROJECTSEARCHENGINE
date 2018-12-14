#!!!CODE FOR CRAWLING ALL THE HTML FILES IN DIRECTORIES/SUBDIRECTORIES!!!
#!!!USING OS MODULE BECAUSE ITS EASIER TO WORK WITH MULTIPLE OPERATING SYSTEMS!!!
#!!!I.E LINUX,UNIX, WINDOWS ETC..!!!
#!!!****************USED DATASET SIMPLE WIKIPIDEA SAMPLE****************!!!
import os;
l = [];#!!!USING LIST TO DETERMINE THE TOTAL FILES IN THE DATASET!!!
for root,dirs,files in os.walk('E:\Data set\simple'):
    os.chdir(root);
    for file in files:
        if file.endswith(".html"):#!!!FILTER THE RESULT AND ONLY STORES HTML FILES!!!
            l.append(file);
            print(os.path.join(root,file));
print(len(l));
