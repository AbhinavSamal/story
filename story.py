from random import choice

when = ["A few years ago","Yesterday","Last night","A long time ago","On 20th Jan"]
who = ['a rabbit','an elephant','a turtle','a mouse','a cat']
name = ['Omi','Vikram','Abhinav','Abhilash','Jeet']
residence = ['Delhi','Washinton DC','Tokyo','Noida','Mexico']
went = ['school','tuition','restaurant','cafe','mall']
happened = ['made a lot of friends','ate a pizza','bought a new pair of shoes','drank coffee','studied science']

print(f"{choice(when)} {choice(who)} named {choice(name)} who live in {choice(residence)} went to {choice(went)} and {choice(happened)}")