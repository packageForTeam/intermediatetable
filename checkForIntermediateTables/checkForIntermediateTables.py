# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:22:40 2020

@author: Dell
"""

import os

def checkForIntermediateTables():
    
    tableName = []
    count = 0
    
    dPath = input("Enter .sql files directory path: \n")
    
    if os.path.isdir(dPath):
        print("\nDirectory exists !!! \n\nSearching for CALL...\n\nModifying..........\n")
        
        for fileName in os.listdir(dPath):
            if fileName.endswith(".sql"):    
                with open(os.path.join(dPath,fileName),'r+') as infile:        
                    for line in infile.readlines():            
                        if 'CALL' in line:            
                            for word in line.split("\'"):
                                tableName.append(word)
                        
                            infile.write("\n\n Create table {} (Select * from {});".format(tableName[1],tableName[3]))
                            count = count + 1
                            tableName = []
                
                            break
            else:
                #print('Not a SQL file !!!\n')
                continue
        print('Modified Successfully {} Files !!!!!!!!!!\n'.format(count))
    else:
        print("Directory not exists...\n")