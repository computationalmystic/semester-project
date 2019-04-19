# Sprint 2, Due April 22, 2019 at 11:59pm

## Feature Backlog

### Augur Teams
1.	Full implementations of your use cases. They can be buggy, imperfect and not exactly right. The point is to get to working code, or "sort of almost" working code and have something to initially show. 
2.	In your updated design specification provide a picture, it can even be hand drawn, that illustrates the connections between your data, your API's, your front end and your use case (i.e., make sure the architecture diagram covers all use cases.)

### Zephyr Teams
1. Provide a "README.md" file that provides a full set of instructions for installing and configuring a version of your system that implements at least one of your use cases. All three is great, but your teams are in different places. 
2. Describe what board's or emulators your final product will use. Be specific. This will be a commitment at this point. 

### RJI Teams
1. I have asked Ed McCain to make time to talk with you about what you have put together thus far, so when you get his feedback, document the specific design or requirements changes that your team may make (or not) based on what you learn.  For example, perhaps he has particular ideas and together he and I arrive at a "faster architecture."  One thought I have as I look through the projects so far is that pictures will likely be uploaded "many at at time", and there may be an organizational structure. 
	- I think rating a folder of photos and enabling the user to put "keep" or "toss" tags (or whatever Ed says) on to each one, and recording that and the rating somewhere you can reference will help the system get smarter in the long run. 
	- You don't have to "do" all the changes this sprint. 
2. Provide a github repository and demo site that provides the ratings for a set of 100 or more photos (and some way of knowing which photo has which rating.)

## General Design

1.	Clarify functional requirement specs for your use cases through conversations with stakeholders via Slack for Augur and Zephyr, and via Ed McCain for RJI> 
	- Document changes and your requirement sources in the Sprint 2 Wiki Page. 
2.	Make any necessary changes to your ERD. Save this new ERD in GitHub and link it to the Sprint 2 wiki page.
3.	Create design document(s) showing 
	- what is necessary for your whole system to work 
		– data sources, 
		- functions, etc. 
		- The full inventory. 
	- Show clearly how the different software components communicate. 
		- Document the reasons for your decisions where you have choices in design. 
		- Save the design document(s) in GitHub and link them to the Sprint 2 wiki page.
	- Think of this activity as a "sufficient" documentation problem. Enough clarity for you and I to both understand what's happening. 
4.	(All Teams) Mock up a full visual design, even it its a pencil sketch, for all the ways users interact with your system.
	- Save a mock-up of your page design in GitHub and link it to the Sprint 2 wiki page.
	- Augur & RJI: Visual/Web
	- Zephyr - Boards, lights, whatever output you expect to be "seen"

## Coding

1.	After analyzing and designing for your data needs: 
	- code the database creation or update SQL (Data Definition Language). 
	- Save this DB creation schema in GitHub and link to it in the Sprint 2 Wiki.
2.	Implement the DB schema, including seed data or “dummy data” for development of any new tables or columns. Basically, create a bunch of bogus data so you can run the application. 
3.	Add all the code for your first full working prototype, following your design decisions, and save it in GitHub. 
	- Also list the files that have been added or changed in the Sprint 2 Wiki.
4.	Identify appropriate unit tests that should be created. 


## Testing

1.	(Bonus for this sprint): Run unit tests you created and document the results in your Sprint 2 Wiki.
2.	Make sure your system runs. Augur/RJI: Check your URL's. Zephyr: Check your README.md.  Remember I have built several of your Zephyr projects in class and office hours, but there's a lot of detail so make sure every can! 

# Sprint 2 Grading Criteria

## 30% of your grade in the second sprint:
- 1 project specific backlog item complete:     B
- All project specific backlog items complete :   A 

## 40% of your grade in the second sprint:
- a. All Design decisions documented, page mock-up included:     B
- b. a, plus All general Design Items Fully Completed:   A– 
- c. a, b, plus ensuring your submission is easily navigated on GitHub using Markdown or the GitHub Wiki. We should not need to click around. It should all be "at the link you submit." :   A 

## 30% of your grade in the second sprint:
- a.	Every function attempted 	B
- b.	a, plus at least 1 full use case functions end to end: 	A-
	- If you run into overwhelming technical issues that keep you from reaching a full end to end use case, provide a clear description (with some technical detail) about 
		- What you did
		- Which parts of the system in your diagram are causing problems/frustations/pain
		- How you tried to address those problems
		- Where you feel you are stuck and what kind help you might need. 
- c.	a, b, plus a brief status update including a list of what is complete, and what is not complete: A

