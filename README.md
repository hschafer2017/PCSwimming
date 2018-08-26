[![Build Status](https://travis-ci.org/hschafer2017/PCSwimming.svg)](https://travis-ci.org/hschafer2017/PCSwimming)

# PCSwimming
PC Swimming E-commerce App - Stream 4 Project

This is a **fictional** ecommerce site, for the nature of this project, for a swim team where swimmers can collaborate and pay team fees, and the community can view upcoming events. Alumni can also post photos of their memories from being on the team. This project is based off a swim team coached by my father in Michigan. 

# Demo
A live demo of this project can be found [here](https://pcswimming-project.herokuapp.com/). This application is hosted on Heroku. 

![Desktop Demo](https://raw.githubusercontent.com/hschafer2017/PCSwimming/master/README_Resources/Swimming.gif "Desktop Demo")

# UX
This site is intended for use by Swimmers and Alumni to allow them further ease of access into what's happening at team events, who is organizing them, a meet schedule, and a place to buy team gear for the season. By paying online, it makes it easier for the coach to keep track of who paid and what they ordered, rather than having to keep track of checks or multiple spreadsheets. 

No template was used to build this site. There were some specific UX and UI designs that were taken into consideration when styling this site. The footer was left off the desktop view to present a cleaner, more minimalistic approach to the design. By adding a footer in the desktop view, I would have risked an awkward contrast in colors to follow the transparent theme of the navbar. However, you can see the footer implemented on pages in the mobile and tablet view, since the background here is off-white. I also did not include it on any pages that are viewed to be 'an extenstion' of another. This was to create a continuous flow of the website, instead of making it constantly seem like you're going to a new page each time you click. 

There are two types of users- Swimmers and Alumni. The swimmers are able to see the discussion board, the shop section, and the events section, while the Alumni only have permission to see the Alumni posts and the events sections. 

When you click to see detail on a product or a swimmer/alumni post, you'll be able to also see all of the other posts or products in the desktop view. I chose this route to stay consistent with the background color scheme throughout the desktop view, and to allow users to toggle back and forth between multiple posts or multiple products without having to constantly go back to a seperate HTML. 
This did pose a bit of an issue with the positioning, however. Since the navy blue size is position:relative and the off-white side is position:fixed, this initially posed a problem when scrolling, especially in the mobile and tablet views. I managed to get around this, however, by altering the height of the panel-body class and adding some extra space at the bottom. I wanted to keep these in a panel to be consistent with the panels used to show events, posts, and products. I chose this 'panel' look because it created a contrast with the navy blue in the desktop, while also creating a nice contrast with the mobile/tablet background via the box shadow. 

With the discussion board for Swimmers, it allows them to discuss team dinners, volunteer opportunities, and other team events. This strives for team inclusivity as all members of the swim team could register for an account. All posts and comments can be monitored by the Coach (a superuser). 

The swimmer on certain desktop pages was a minimalistic way to fill the off-white space on the right half when there was nothing selected. 

I wanted to implement an ease of access with this site, to make it as simple and obvious as possible for both swimmers and alumni to navigate through the site while maintaining consistency throughout the design. 


# Testing
## Automated Testing  
All automated testing was done using Travis-CI. 
There is automated testing done for all apps with views, models, and forms (where applicable). The testing currently provides 86% coverage for the app. There is quite a bit of repetition in the testing, however, I would like to further refactor them and implement more specific tests for more coverage at a later date. 

During testing, I realized that since I have two different user types, swimmers and alumni, there was nothing stopping a swimmer from typing in the URL to an alumni page and being able to access it and visa versa. To resolve this glaring security issue, I implemented a try/except into the views that required the function to check whether or not the user had the Swimmer (or Alumni) model associated with their user account. If the logged in user did not have the appropriate model associated with their user account, then they will be given an HttpResponseForbidden (403 error) when trying to access the page. The superuser is permitted to access both Swimmer-specific pages and Alumni-specific pages. Furthermore, I implemented an if statment to redirect the user to the login page if they were not authenticated (an AnonymousUser), and if they were authenticated to then run the try/except. 


Coverage was tested by running the following in the command line: 
```
$ sudo pip3 install coverage 
$ coverage run manage.py test (app name)
$ coverage html
```
This will create a htmlcov folder. There are a bunch of files in this folder, so I included them in the .gitignore. 

To view the percentage of your app that's being tested for, open a new idle, and run the command 'htmlcov/index.html' in the idle. By clicking the link that appears when you run, it will be able to see the coverage in a new window. You can also view that all of your tests are passing by running the following in the command line: 
```
$ python3 manage.py test
```
To view the coverage report in the command line for the entire project, run the following commands, alternatively, you can run the report for just one app by only including that app in the source: 
```
$ coverage run --source=alumni,accounts,events,home,products,cart,posts,checkout manage.py test
$ coverage report
```

## Manual Testing: 
Manual testing was done for all edit/post/delete/appearance functions in both the events and posts apps. This was to ensure that what was supposed to be deleting was deleting, and that only designated users (the post/comment owner or the superuser) was able to delete/edit the content selected. I also verified that the correct author showed up for the posts and comments. All links and forms are verified to be working correctly via manual testing. 

The Stripe payment function has been verified with a test card and all transactions show up on the Stripe dashboard. 

![Stripe Test Cart Payment](https://raw.githubusercontent.com/hschafer2017/PCSwimming/master/README_Resources/payment.png "Test Card Payment")

# Features
Only the head coach has access to the admin page. Since it is their team's site, it makes it easier for them to monitor all account activity and blog content. They are the only ones who will be allowed to make master changes to the site. This site has ecommerce and blog functionality. Payments are processed through Stripe, and since it is a fictional site, it only processes 'test card payments.' The events section allows the public, alumni, and swimmers to see upcoming events. 

The Shop section allows swimmers to pay their dues and purchase team-related equipment for the season. They are able to write in a size, as suits, caps, jackets, and other team apparel do not all follow the S, M, L, XL format. Sizes options are listed in the product's detail. 

The Discussion (Posts) and Alumni sections have different apps because the goal was to keep them as seperate as possible, as if they were included in the same app, there would have been too much content in one app. Also, there would have needed to be sorting of the type of author of the post (swimmer or alumni), and while it would have not been an issue if a swimmer or alumni was viewing it, it would be a bit of a mess for the coach to view. Also, there are certain fields that the Alumni Post Form has (images, for example) that the Post Form for the Swimmers doesn't have. 

The Discussion also allows the ability to create, edit, and delete comments as well as posts. This way, swimmers are able to comment on posts asking for volunteers or with questions from previous content posted. 

The Events section allows both Swimmers and Alumni to view upcoming events, which include the date, location, opponent, and any other useful information relevant to the meet. 

## Features Left to Implement
I would like to make the alumni section more sophisticated to allow the alumni to donate to the swim program. Furthermore, I would like to also create seperate user group categories accessible from the admin page. This functionality would allow the coach to send out an email announcements to all swimmers, all alumni, or everyone registered from the admin page via the admin page. I would also like to create another user group for parents of swimmers to allow them to discuss team dinner planning, transportation, and other team-related matters that don't necessarily concern the swimmers. 

I would also like to make modals for new posts and comments on the desktop instead of redirecting to a new page. I think this could improve the overall flow of the UX for desktop users. 

For products, I would also like to implement an option to choose a size, so that team members can purchase their team suits through the site individually specifying their size, along with other apparel that is size-specific. The issue I ran into here, is that swim suits are in numeric sizes (28, 30, 32, etc), while jackets, t-shirts, and other apparel follow the small/medium/large format. Also, certain products, like team dues and equipment, will not have a size. I would like to make it so that some products have a size option (that can vary depending on the product) and some don't. 

I hope to implement this website for commercial use by setting up the payment functionality to process real credit cards. 

# Credits 
## Content 
All content in the Events, Alumni, Discussion, and Shop sections is fictional and written by me, or courtesy of Portage Central Swimming and Diving. 

## Media 
The PC logo was provided by Portage Central Swimming and Diving. 

## Acknowledgments 
The media query for the collapsed navbar regardless of viewport width was taken from this [site](https://www.codeply.com/go/iaM1zcNsQB/bootstrap-navbar-always-collapsed). 

For the post comments, I followed the Django Girls Tutorial [here](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models/), however, it was significantly modified to fit my project, and the ability to edit and delete comments was added. 

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