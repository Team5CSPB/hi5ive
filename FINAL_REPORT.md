# Penta5ive

## Project Title
hi5ive

## Team Members
- Lerena Holloway
- Daniel Simonson
- Derek Larson
- Matthew Martin
- Christa Sparks

## Project Tracking Software
[Link to Trello Board](https://trello.com/b/sBgqNqyE)


## Weekly Status for hi5ive

## Link to 5 minute video: a demo for a potential customer
[Link to Video Demo](https://youtu.be/8SnDZlPyweA?si=qKxDhncBXccCmSz4))

[Presentation Slides](https://docs.google.com/presentation/d/18C0lSGMVN8QgwIJdxYUt9PAw9BzccHCpdvyjWSQA7qU/edit?usp=sharing)


## Version Control Repo Link
[Github](https://github.com/Team5CSPB/hi5ive)

## Reflections

* What you completed
* What you were in the middle of implementing
* What you had planned for the future
* Any known problems (bugs, issues)

### Frontend: ###

The frontend team successfully created a home page that displayed our brand logo, a paragraph about our project, as well as an image slideshow to enhance user experience , and a signup and login button that would  redirect the user to those respective pages. The team also completed a signup page, which accepted numerous fields like name , email , password , etc in order to sign the user up, as a login page that would log the user into the website. The frontend team also completed a matches page that would display potential matches and could be filtered by interest, with a match button available to match those user. The profile page also completed and displayed interests, groups, profile pic, and other pertinent information. 


Features in the middle of being implemented were mainly various degrees of deeper functionality to our project. For example, we want to be able to connect to our database and pull users using the backend to be displayed as potential matches , as well as being able to set and change our interests in the user profile page. There were some CSS formatting changes that were in progress that would format the user profile pics appropriately and standardize all the styling in the app. 

Frontend plans for the future involved creating some type of user authentication to login to the site and create users. The team wanted to create a separate section in the user profile page that would display the actual matches as well. In the future once these were done, together the team would work on expanding a match between two people to a match between larger groups of people based on interests.

### Backend ###

We built our back end using the Flask server framework in python. This handles back end routes, providing endpoints for the front end to retrieve data. The backend facilitates communication with the database to find users by id, find users by interests, create matches between users. The routes are partially implemented as the project stands, the next to be added are login/logout along with a flask CORS system for verifying login credentials and login status, with signup/create_user and delete user soon after. Currently our database is filled with dummy data for database and route testing. Error handling is pretty good in its current state but it could use a little more, especially as we expand interaction with the front end for more complex operations than just database retrieval. I would also like to implement some interaction with an image hosting api as suggested in the presentation for our profile pages, as they are just stock photo placeholders right now.

### Database ###

We created a database using PostgreSQL and deployed it on render as a persistent development database. This includes all necessary tables and fields for accomplishing our project goals. We also implemented scripts for filling and testing the database with dummy data.

Plans for the future were to implement more tracking fields, like more detailed location services, that could help narrow down the search for matches. As well as creating data cleaning protocols to ensure the safety of our data.

The current bugs seem to be between deployment and the backend being filled with an old version of the database that made the routes unable to correctly request all data. 

## Render Links
[Hi5ive Flask](https://hi5ive-flask.onrender.com)

[Hi5ive React](https://hi5ive.onrender.com)
