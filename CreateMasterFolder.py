import sys
import json
import subprocess
import time

def JenkinsFoldercreate(MasterFolder,domain):
    CommandFolder="java -jar Lib\jenkins-cli.jar -s http://xsnw50f525a:8080/ create-job Deploy_Check/"+MasterFolder+" --username admin --password admin <input\FolderTemplate.txt"
    print(CommandFolder)
    subprocess.Popen(CommandFolder,stdout=subprocess.PIPE, shell=True)

    time.sleep(15)

    CommandDomainFolder = "java -jar Lib\jenkins-cli.jar -s http://<jenkinshost>:8080/ create-job Deploy_Check/"+MasterFolder+"/"+domain+" --username admin --password admin <input\FolderTemplate.txt"
    print(CommandDomainFolder)
    subprocess.Popen(CommandDomainFolder,stdout=subprocess.PIPE, shell=True)




