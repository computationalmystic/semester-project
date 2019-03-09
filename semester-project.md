# Semester Project

## Your Mission:
1.	There will be more requirements than you can satisfy, but you want to document all of the ones that you can identify.  Both functional, non-functional, user and system.
2.	Consider how you are going to keep track of requirements?
	- Will there be a hierarchy?
	- How will you validate with Stakeholders?
	- What is a sufficient design to justify your efforts this semester.
 
## Create a Development Environment
2. Install Anaconda for environment management of python version 3.7 https://www.anaconda.com/distribution/ 
	- Question: What if I want to write C code for the Zephyr project? 
	- Answer: Nearly every software distribution system these days uses python for *something*, and Anaconda is a good environment for managing different python environments on the same computer
3. Create an anconda environment for testing purposes: 
	- `conda create -n yourenvname`
	- `conda activate yourenvname`
	- Exit terminal
4. Get yourself an API Key for GitHub: 
	- https://github.com/settings/profile (make sure you are logged in)
	- https://github.com/settings/tokens 
	- "Generate new token"
	- Select all permissions EXCEPT "delete repo"
	- Copy the token and put it in a place where you will be able to find it again. If you do not do this you cannot ever get the token again and you have to generate another one. 
1. Go to https://github.com/chaoss/augur 
2. Star the augur repository
2. Fork the augur repository
2. Follow the README.md instructions to configure and install augur using vagrant. 
	- Question: Why would I do this if my team is not doing the Augur project? 
	- Answer: Because follwowing these instructions gets you setup with vagrant and virtualbox, will will help you to manage your development environments. 
	- Run Augur
	- Two current issues require you to take a few steps after running the `augur` command fails: 
		- `sudo pip3 install --upgrade .`
		- Copy the `augur.config.json` file from [here](./augur.config.json) and make it the one in your main augur directory. 
	- If you encounter any additional issues open an issue on the repository
	- At the very end you are going to need that token to the augur.config.json file
	- To test augur, within your vagrant box at the command line and after following all the readme instructions on the augur project:
		- `make dev-start`
		- navigate to http://localhost:3333 in your browser

## Choose a Project
*Design Goal Options for each project* : 
1. Using the Linux Foundation's Zephyr project, build a "smart home" system to suit the needs of a family that has two infant twins and a 12 year old. And a grandparent living in a downstairs apartment.  
	- User Proxies: Your own experiences and family
	- Project Pages: https://www.zephyrproject.org/ 
	- Pre-Installation: Start your Augur vagrant box, or create your own vagrant box (borrowing Augurs will be easier!)
	- Start the box up following the instructions here: https://github.com/chaoss/augur/blob/master/README.md 
	- mkdir `your project name`
	- cd  `your project name`
	- Installation Instructions: https://github.com/zephyrproject-rtos/zephyr
		- Getting Started Guide: https://docs.zephyrproject.org/latest/getting_started/index.html
		- Make a Zephyr "Hello World" app: https://docs.zephyrproject.org/latest/samples/hello_world/README.html#hello-world 
2. Using the CHAOSS working group's Augur project, add an example of a data drill down user interface for commits on git repositories. 
	- User Proxies: Sean Goggins, http://chaoss.community 
	- Installation: (you already have augur installed from the dev env steps)
	- Project Pages: http://www.augurlabs.io / https://github.com/chaoss/augur 
3. Reynolds Journalism Institute 
	- User Proxies: Ed McCain
	- Pre-Installation: Start your Augur vagrant box, or create your own vagrant box (borrowing Augurs will be easier!)
	- Start the box up following the instructions here: https://github.com/chaoss/augur/blob/master/README.md 
	- mkdir `your project name`
	- cd  `your project name`
	- Installation
		- Medium Article and associated software: 
			1. https://medium.com/idealo-tech-blog/using-deep-learning-to-automatically-rank-millions-of-hotel-images-c7e2d2e5cae2
			2. https://github.com/idealo/image-quality-assessment/tree/master/models/MobileNet
			3. https://keras.io/applications/
	- Google’s “NIMA” : https://ai.googleblog.com/2017/12/introducing-nima-neural-image-assessment.html
	- GitHub Image Quality Assessment Topic: https://github.com/topics/image-quality-assessment
	- Python Image Quality Assessment Library: https://pypi.org/project/sewar/
	- Another Python Image Assessment Library: https://pypi.org/project/pybrisque/



# In class today, you will: 

## Today’s Tasks:
1. (10 minutes) Select a project
1. (45 Minutes) Identify the categories of requirements that need to be captured in your requirements document. This would be a top level document where you put the major types of requirements, and list a few examples of those requirements. (For Example, “Project Commits, Project Issues, Issues over time, etc. ”)
1. (10 Minutes) Revisit your project choice 
2.	(30 Minutes) Tech Setup
	- Name your GitHub Repo and Get Dr. Goggins to create it for you. In our GitHub organization
	- Ask any questions that you want to about your deployment, but make sure you can deploy some simple code from your GitHub repo to some kind of server environment.

# Sprint 1 : Requirements and Tech Config Setup

	- 2019 CS4320/7320 Software Engineering
	- Group Assignment: Semester Groups 

## Problem
*whatever you chose* 

## Notes on the Assignment Completion Strategy
Complete the steps below, presenting the information in an organized fashion. When you are finished, one of you submit a link to your group wiki page to Canvas. Note the details under Step 4 regarding other document requirements.
	- Your “language of construction” for all text based work in your repository is “markdown”. You should familiarize yourself with this page so that you can use the markdown syntax easily.  https://daringfireball.net/projects/markdown/syntax … 
	- The measure of success for “.md” files (which are different than the wiki in this assignment” is, “do they render in a markdown preview editor like “atom” ( http://atom.io )? **It is not “do they render on GitHub”?** This is because GitHub’s markdown syntax is not exactly the same as most people use, and I would rather require you to learn a method that is not GitHub dependent. 

### Step 1
1. 	In this exercise, you will create use cases for the semester project, which is based on the needs of stakeholders in the project you selected. Your first step is to find a software program that you can use to draw use case diagrams. You’re welcome to use any program for this assignment. Here are a few suggestions:
	- yEd: http://www.yworks.com/products/yed (Links to an external site.)
	- Microsoft Visio or Powerpoint 
	- Sketchbook: https://sketchbook.com/?locale=en (Links to an external site.)
	- Violet UML Editor: http://alexdp.free.fr/violetumleditor/page.php (Links to an external site.)
	- Draw IO : http://www.draw.io (Links to an external site.) (recommended by Jeremy)
	- We will also accept neatly drawn hand diagrams, but make sure you know how to write use case diagrams. 

## Step 2
1. Familiarize yourself with your Stakeholders. Seek information about requirements in the slack channel for your project. There will be people in the channel during the coming weeks.  This is your chance to get feedback and ideas directly from Stakeholders. Remember your proxy stakeholders:
	- Zephyr: Your family and experiences, the specifics of the design case
	- Augur: Sean Goggins, community sites. 
	- Reynolds Journalism Instistute, Ed McCain: Sean Goggins will facilitate a meeting with Ed McCain and his team next week, after the exam. 

## Step 3
1. You should prepare a sufficient number of use cases to serve the purpose of scoping your team’s semester project. This may not be the final version of the requirements.  We are beginning with use cases because they are high level at the outset, and form a solid foundation for keeping your team centered on how to get the work done. I suggest the following steps: 
	- Complete step 2
	- Make a list of actors for the use cases
	- Make a list of tasks/actions that constitute the use cases
	- Create use case diagrams and short descriptions 
	- Ask questions of your stakeholders using the slack channel
	- Iterate on the use cases; possibly changing some, dropping some and adding some. 
	- [Follow this template for use cases](_use-case-template.md)
1. Your team is responsible for several use cases. Each individual should contribute to three different use cases, through either independent design, design collaboration, or careful peer review of a finished diagram. 
	- Carefully plan responsibilities for design and peer review so each individual works on three different use cases. 
	- Your team and your requirements should span 3-5 use cases. More is not better. Go for coherence and sufficiency.  
1. Each use case should contain the following elements:
	- Title (active verb phrase, states main goal)
	- Description (This may be several paragraphs. Context is important. You are describing the use case in some detail, and since many of the use cases will involve users changing parameters on data visualizations, you should be exceedingly clear about this type of thing.) 
	- Triggers (What prompts the use case to start?)
	- Actors (Who is involved?)
	- Preconditions (This includes things like “data loaded”. Or, project is flagged as “of interest”; etc.)
	- Main Success Scenario (Goals) (What does it look like when the user’s work is successful in the system?)
	- Alternate Success Scenarios (For a data analysis and “data playing” focused project like this one, there could be several different success scenarios for each use case. “Sees visualization” is not a success scenario. “Compares four different projects on “indicator X” and saves “project trackers” for each one could be a success scenario.)
	- Failed End Condition (“crashes” is not a failed end condition. “User is unable to discern the difference between two projects because they are similar on the available indicators” might be). 
	- Extensions
	- Steps of Execution (Requirements)
	- A use case diagram, following the UML Standard for expressing use cases. 

## Step 4
1. Review each use case as a team.
	- Provide a full list of use case pages in markdown format in your repository (to be created)
	- Each use case should have a title. Each use case diagram should be captioned. You should succinctly describe the actors and activities in the caption. When you caption something “use case diagram” with no further explanation you are wasting both your own time and the reader’s!  
	- Each diagram should indicate who worked on it and in what role.
1. Your work will be assessed on the completeness, consistency, clarity and notational correctness of your group use cases. 
1. This first spring Group Assignment is due in Canvas at 11:59 pm on Friday, March 22.
1. Each member of your team will also submit an assignment demonstrating they have their development environment configured. **this will be due on Friday, March 15**   
 
## Step 5
1. Deploy your project repository, even if it is only a "hellow world" page. 
 
