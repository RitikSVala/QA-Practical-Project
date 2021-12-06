# Random Rap Name Generator:
This repository is for the QA Practical Project Task.


## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI/CD Pipeline](#CI/CD-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

## Project Brief:  
The application that I have developed is a simple generator that randomly pulls down from a database of already existing rapper names and dates of when their best albums were released. The user has to simply write in their full name & hit submit which will then show a display message that will present the user with a randomly selected rapper name & a date of when their best album was released. I tried incorporated the flask framework and parts of the CRUD functions as my application is able to create, read without the functionality of being able to update previous records.
As the requirements had stated the choice of what I wanted the project scope was up to me and I was able to get as creative as I wanted to but I had to abide by the requirements and have four separate micro services which would be connected to one another and work hand in hand through GET/POST. 
 
![Picture1](https://user-images.githubusercontent.com/92307241/144778866-78e51afb-55d4-4687-892d-17c04bd800d2.png)

## Project Planning:
* Jira for project tracking
* Git for version control
* Jenkins as a CI server
* Ansible for configuration management
* GCP cloud platform
* Docker as a containerisation tool
* Docker swarm for container orchestration
* NGINX as a reverse proxy



## App Design: 

Service 1 = front-end: This service was what allowed the user to connect to the application as it is where everything is displayed and presented for the user to interact with as well as where all the printout functions (random generations) are printed. The function to add names to the list

Service 2 = name-api: This service receives HTTP GET requests from service 1 and then randomly chooses a rapper name from the database.

Service 3 = date-api: This service receives HTTP GET requests from service 1 and then randomly chooses a date from the database.

Service 4 = display-api: This service receives HTTP POST requests from service 1 and then prints the final display message which is shown to the user as their desired result.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible.


## Screenshots of application:  
Below you can see a screenshot of the main home page for my application, 
![Picture2](https://user-images.githubusercontent.com/92307241/144778996-2bb983ab-7c3e-4e33-82cd-c0197a6297ce.png)


Below you can see a screenshot of the screen where the user is able to add their own rapper names and dates
![Picture3](https://user-images.githubusercontent.com/92307241/144779009-3160f234-46d3-4f44-8d9d-72e7a1fbd957.png)


Below you can see a screenshot of the list of random rapper names and dates beside them.
![Picture4](https://user-images.githubusercontent.com/92307241/144779018-ef01b998-bf44-46e5-b1a2-1e782a1420c7.png)


## CI/CD Pipeline:
This project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
* Project tracking
* Version control
* CI server
* Deployment environment 

 I decided to use Jenkins to show the stages for this project through a CI Pipeline. Jenkins allowed me to structure my work through a timeline and define the requirements that would make my project functional from a user perspective. I created my User Stories to better understand what I would need and how my tasks could be broken down between the three days I had to complete this project whilst meeting all of the requirments.

 Version Control (GIT) For version control, I used GitHub to manage my project as it allowed me to directly upload and save my work onto my repository without having to create a local back up. It has also allowed me to go back to previous versions of my work to pull down any work that could be useful if I managed to create issues with the file version on my local machine.

Project tracking was done using Jira. Tasks were assigned to epics which were categorized so that I knew what tasks had to be completed in what order. Splitting them into seperate epics allowed me to split my work into sections that I could strategically plan out in order what tasks needed to be completed before one another.

![Picture5](https://user-images.githubusercontent.com/92307241/144779150-93dc0878-cc5f-41f1-bac4-9937887b140f.png)

Wrote docker file for each application to generate the docker images and publish them into docker hub.
Once I had the docker file generated I docker composed the file to build the images based on the docker file and deploy the application.
Within docker compose file I also added the nginx file which will be listening on port 80 which will then redirect the users request to the front-end service. (Reverse proxy) This is to increase the security of the application. 
Created a Jenkins pipeline to build the images using docker compose, publish the images & run ansible playbook to provision infrastructure for all the instances as well as deploy the application. I then created a GitHub hook which will trigger the Jenkins pipeline whenever there is code being pushed up into the repository. 

![Picture6](https://user-images.githubusercontent.com/92307241/144779295-9a828e61-8c57-4f59-a04d-dfa8b368ad9c.png)


## Risk Assessment:

Risk Assessment: I created a table that would be my risk assessment table so that I could better understand the risks of the project and what it could potentionally be vulnerable to. Within having done this research it allowed me to strategize ways to control this.

![Picture7](https://user-images.githubusercontent.com/92307241/144779262-b86b63e6-d026-4da8-bd2e-0933881994f1.png)


## Testing:
Testing: I was unable to get my tests to work due to a magnitude of technical reasons. 
However I did attempt to use pytest within my project and unfortunatley was unable to get it to work.


## Known Issues:
* I was unable to get tests to work, as I got them to run for the same project but without the 4 microservices with 100% coverage 
* The website links from front-end service aren't functional and shows that the programme in itself is dysfunctional however works on local machine.
* Pytest was unsuccesfull 

## Future Improvements:  
* I would try to incorporate more of the CRUD functionalities so that users can update/ make changes to the names and dates they have added as well as delete ones that they dislike.
* I would also like to try and make it so that the application gives more than just 1 random output where the users can pick between 2 random generated rap names.
