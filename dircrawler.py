import os;
l = [];
for root,dirs,files in os.walk('E:\Data set\simple'):
    os.chdir(root);
    for file in files:
        if file.endswith(".html"):
            l.append(file);
            
             #print(os.path.join(root,file));
print(len(l));
