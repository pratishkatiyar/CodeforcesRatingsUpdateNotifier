import json   
import urllib.request  
from urllib.error import URLError
import time
import subprocess as s
import os

print("Enter Contest Id")
id=input() # contest id

print("Enter your handle")
user = input() # user handle

url="https://codeforces.com/api/contest.ratingChanges?contestId="+id
f=True;
while(f):
    try:
        with urllib.request.urlopen(url) as urli:
            data = json.loads(urli.read().decode())
            size=0
            if(data["status"]=="Failed"):
                time.sleep(1)
                continue
            old_rating=0
            new_rating=0
            participated=False
            for x in data["result"]:
                # print(x)
                if x["handle"] == user:
                    participated=True
                    old_rating=x["oldRating"]
                    new_rating=x["newRating"]
                size+=1
            if (size>0):
                f=False
                delta=new_rating-old_rating
                if(participated):                
                    s.call(['notify-send','Codeforces','Rating are Updated! your delta is '+str(delta)])
                else:
                    s.call(['notify-send','Codeforces','You not participated in the contest!'])
            else:
                time.sleep(1)
    except URLError as e:
        # print("trying..")
        time.sleep(1)


