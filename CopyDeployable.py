import sys
import os
import subprocess
import json
import time


def Copyfiles(domain):
    with open('input/admin.json') as adminjson:
        admindata = json.load(adminjson)

    targetserver = admindata[domain]['admin']
    drive = admindata[domain]['drive']
    createfolder = "paexec \\\\"+targetserver+" cmd.exe /c mkdir "+drive+":\Deploy_Check\\"+domain
    print("Creating folder with command - > "+createfolder)
    subprocess.Popen(createfolder,stdout=subprocess.PIPE, shell=True)
    #stdout, stderr = process.communicate()
    #print(stdout)
    time.sleep(60)
    print("Folder ccreated, starting files transfer\n")
    copyear="copy output\LogWriter.ear \\\\"+targetserver+"\\"+drive+"$\Deploy_Check\\"+domain
    copyxml="copy output\LogWriter_"+domain+".xml \\\\"+targetserver+"\\"+drive+"$\Deploy_Check\\"+domain
    copycred="copy output\\"+domain+"_cred.txt \\\\"+targetserver+"\\"+drive+"$\Deploy_Check\\"+domain
    subprocess.Popen(copyear,stdout=subprocess.PIPE, shell=True)
    print("EAR is copied"+copyear)
    subprocess.Popen(copyxml, stdout=subprocess.PIPE, shell=True)
    print("XML is copied" + copyxml)
    subprocess.Popen(copycred, stdout=subprocess.PIPE, shell=True)
    #subprocess.Popen(createfolder, stdout=subprocess.PIPE, shell=True)
    print("CRED is copied" + copycred)

