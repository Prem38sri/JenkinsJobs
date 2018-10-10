import sys
import time
import XMLGenerator as XMLCreate
import CopyDeployable as Copyfile
import CreateMasterFolder as JobFolder
import CreateDeployJob as jdeploy
import CreateUneployJob as jundeploy
import CreateDeleteJob as jdelete

project="project"
domain="domain"

print("Calling XML Generator\n")
XMLCreate.XMLGenerate(domain)
print("Calling Copy Generator ")
Copyfile.Copyfiles(domain)
JobFolder.JenkinsFoldercreate(project,domain)
time.sleep(20)
jdeploy.JenkinsCreateDeployJob(project,domain)
time.sleep(20)
jundeploy.JenkinsCreateUndeployJob(project,domain)
time.sleep(20)
jdelete.JenkinsCreateDeleteJob(project,domain)