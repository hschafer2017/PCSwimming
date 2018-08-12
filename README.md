[![Build Status](https://travis-ci.org/hschafer2017/PCSwimming.svg)](https://travis-ci.org/hschafer2017/PCSwimming)

# PCSwimming
PC Swimming E-commerce App - Stream 4 Project

This is a **fictional** ecommerce site for a swim team where swimmers can collaborate and pay team fees, and the community can view upcoming events. Alumni can also post photos of their memories from being on the team. 

# Demo
A live demo of this project can be found [here](https://pcswimming-project.herokuapp.com/). This application is hosted on Heroku. 


# Testing
## Automated Testing  
All automated testing was done using Travis-CI. 
There is automated testing done for accounts. 

Testing was done by running the following in the command line: 
```
$ sudo pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html
```
This will create a htmlcov folder. There are a bunch of files in this folder, so make sure to include them in the .gitignore. 

To view the percentage of your app that's being tested for, open a new idle, and run the command 'htmlcov/index.html' in the idle. By clicking the link that appears when you run, it will be able to see the coverage in a new window. You can also view that all of your tests are passing by running the following in the command line: 
```
$ python3 manage.py test
```

## Manual Testing: 
Manual testing was done for all edit/post/delete/appearance functions in both the events and posts apps. This was to ensure that what was supposed to be deleting was deleting, and that only designated users (the post/comment owner or the superuser) was able to delete/edit the content selected. I also verified that the correct author showed up for the posts and comments. 

# Features
Only the head coach has access to the admin page. Since it is their team's site, it makes it easier for them to monitor all account activity and blog content. They are the only ones who will be allowed to make master changes to the site. This site has ecommerce and blog functionality. Payments are processed through Stripe, and since it is a fictional site, it only processes 'test card payments.' The events section allows the public, alumni, and swimmers to see upcoming events. 

The Shop section allows swimmers to pay their dues and purchase team-related equipment for the season. By paying online, it makes it easier for the coach to keep track of who paid and what they ordered, rather than having to keep track of checks or multiple spreadsheets. 

The Discussion (Posts) and Alumni sections have different apps because the goal was to keep them as seperate as possible, as if they were included in the same app, there would have been too much content in one app. Also, there would have needed to be sorting of the type of author of the post (swimmer or alumni), and while it would have not been an issue if a swimmer or alumni was viewing it, it would be a bit of a mess for the coach to view. Also, there are certain fields that the Alumni Post Form has (images, for example) that the Post Form for the Swimmers doesn't have. 


## Features Left to Implement
I would like to make the alumni section more sophisticated to allow the alumni to donate to the swim program. Furthermore, I would like to also create seperate user group categories accessible from the admin page. This functionality would allow the coach to send out an email announcements to all swimmers, all alumni, or everyone registered from the admin page via the admin page. I would also like to create another user group for parents of swimmers to allow them to discuss team dinner planning, transportation, and other team-related matters that don't necessarily concern the swimmers. 

# Credits 
## Content 
All content in the Events, Alumni, Discussion, and Shop sections is fictional and written by me, or courtesy of Portage Central Swimming and Diving. 

## Media 
The PC logo was provided by Portage Central Swimming and Diving. 

## Acknowledgments 


# Plug-Ins 
If you have the Grammarly plug-in in your browser, when you click on a form's textarea to create or edit a post or comment, the textarea box will jump to the top of the page and then reposition itself into the designated input area on the page. The plug-in will still work, and you will still be able to add and edit content if you're using the plug-in. If the plug-in is turned off, there is no issue with the textarea jumping around the page. Read more about this issue with the Grammarly plug-in [here](https://stackoverflow.com/questions/47957205/textarea-box-moving-on-click-on-initial-page-load). 

# Installation 
If you're interested in cloning this repository, to set up and install everything in the requirements.txt run the following command in the terminal: 
```
$ sudo pip3 -r install requirements.txt
```
Then, detatch from my repository using the following command: 
```
$ git remote rm origin
```

Please note that I used Cloud9 for this project, so if you are using a different editor, the terminal commands may differ. Please consult the docs for the editor you're using for further information on editor-specific terminal commands. All secret keys for AWS, Stripe, Production, and Django Settings in Heroku will need to be obtained individually, as they are hidden. You can find a secret key generator for Django [here](https://www.miniwebtool.com/django-secret-key-generator/). 