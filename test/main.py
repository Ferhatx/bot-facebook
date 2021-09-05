# -*- coding: utf-8 -*-
import hashlib
import csv
def main():
    
    url=[]
    
  
    with open("urls.lst") as file:
        for reads in file:
            result=hashlib.md5(reads.encode()).hexdigest()
            url.append([[reads],[result]])

    with open('url-md5.csv','w',newline='') as file_csv:
        writer=csv.writer(file_csv)
        writer.writerows(url)
    
    print(url)
        

   

if __name__ == "__main__":
    main()