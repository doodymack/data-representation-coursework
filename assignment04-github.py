# assignment04-github.py

# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# The program should then commit those changes and push the file back to the repository.
# I do not need to see your keys
# (see lab2, to follow)


# to use this install package  pip install PyGithub  (installed in command terminal)
from github import Github

# import require libraries
import requests

from config3 import config as cfg
# api key from config file for private repository
# cannot upload to github.  Thus cannot run code remotely
# I am posting a word file with screenshots before and after code run to the 
# data-representation-coursework 

apikey = cfg["githubBPRkey"]

#create a variable with apikey to pass to Github 'get_repo' function
g = Github(apikey)

repo = g.get_repo("doodymack/BigProject")

#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")

urlOfFile = fileInfo.download_url
#print (urlOfFile)

# download file (test.txt)
response = requests.get(urlOfFile)

# save text to new variable contentOfFile
contentOfFile = response.text

# use python 'replace' to replace str A for str B
# save updated text in new Variable NewContentOfFile
NewContentOfFile=contentOfFile.replace("andrew","paul")

#print (contentOfFile)
#print (NewContentOfFile)

# reupload the file to github repository
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",NewContentOfFile,fileInfo.sha)
print (gitHubResponse)


# CODE NOT NEEDED

#for repo in g.get_user().get_repos():
#    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
# make sure this replository exists, and that the path is correct

#newContents = contentOfFile + " more stuff 2 \n"
#print (newContents)
#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)