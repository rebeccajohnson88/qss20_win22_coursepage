# Evaluation and grading

## Summary and grading policy

You will have four cumulative late days for assignments, that can be apportioned as you see fit between the problem set one and problem set two. Late days cannot be used for the final project or final presentation. If you run over and have not submitted the pset by the following Monday, I ask that you not attend class as not to see the answers. There will be a deduction of 10 percentage points for each late day after you have used your allowed late days.

Grades may be curved if there are no students receiving A's on the non-curved grading scale. 

## import modules
import pandas as pd

from IPython.display import display, HTML

grade_summary = pd.DataFrame({'Assignments':
                ["Datacamp modules",
                  "Two problem sets",
                  "Final project",
                  "Team player/participation"],
                'Percentage':
                [5, 
                  50,
                  35,
                  10],
                'Deadlines':
                ["Throughout",
                  "Pset one: Thurs. 04-15; \
                  Pset two: Thurs. 05-13 and Tues. 05-18",
                  "Presentation: Tuesday 06-01; Short report: Sunday 06-06",
                  "Throughout"]}) 

HTML(grade_summary.to_html(index=False))

## Details

### Datacamp modules to support programming topics (5% of grade)

The DataCamp modules are mainly to support your work on the problem sets and final project by giving you additional practice prior to our in-class activities. As a result, they will be graded on a "complete" and "incomplete" basis, regardless of how many points you received on the assignment itself. This means that you shouldn't get stuck partway through, since you can always ask to be shown the answer with a points deduction. Conversely, if the concepts are review, these should be very quick to complete, but if you'd prefer to skip, you can talk to me and I will reapportion the 5\% to your second problem set.

### Two problem sets (25% of grade, each; 50% total)

DataCamp provides a very smooth introduction to programming, in the sense that they provide you with example code that gets you ~80\% of the way to the solution, with you needing to apply that code to reach the other ~20\%. 

In contrast, the two problems sets will assess your ability to apply the concepts to data that is substantially messier, and problems that are substantially more difficult, than the ones in the DataCamp modules. More details on the problem sets will be provided the week before each is released,  but roughly, the workflow will be:

- Accessing the problem set and data via GitHub and/or jhub
- Working to produce the following outputs for each problem set:
  - A raw .ipynb (or .Rmd file) with the code for the pset
  - A compiled pdf that displays that code, as well as the answers to the written questions. These written questions will involve using some Latex syntax for equations and formatting.
  - When applicable (e.g., part of the pset is run in script form), a supporting .py or .R file
  
The problem sets will be graded on both accuracy and programming style. For instance, by our second problem set, you will have learned to write functions. The problem set will be designed to test those concepts and if you revert, for instance, to writing repeated code that could be replaced with a function, points will be deducted even if that inefficient code arrives at the correct answer. 

**Collaboration**: problem set one will be 80\% group based and 20\% individual (each person will submit a single problem set reflecting the work of the group for the first 80\% and your own work for the individual problem). Problem set two will be fully individual. You should ask all questions on Slack in public channels and I may ask you to delete a post if it shows too much of a solution.

### Final project (35% of grade)

- I will randomly assign groups of 3-4 a few meetings in to the quarter. I've found that this is more effective than letting you choose your own groups for teaching you how to collaborate on technical projects with people who you may not always see eye to eye with!
- I'll be releasing instructions on Canvas for two preliminary project milestones 
- Each group will work on a project that integrates the concepts we are covering into an applied data science project. The end product will be a github repository that contains:

  - The raw source data you used for the project. This will include portions of the data I provide to all groups and external data sources you bring to the project.
  - A pre-analysis plan where you pre-commit to certain analyses with the data: this will be especially important for the other group to be able to replicate your work.
  - A README for the repository that, for each file, describes in detail:
    - Inputs to the file: e.g., raw data; a file containing credentials needed to access an API/
    - What the file does: describe major transformations.
    - Output: if the file produces any outputs (e.g., a cleaned dataset; a figure or graph).
  - A set of code files that transform that data into a form usable to answer the question you have posed in your descriptive research proposal.
  - Final output: 
    1. A 10-minute presentation, written in Beamer (presented in class on **Tuesday June 1st**).
    2. A report written in the computer science-style conference proceedings (10 pages; will share a template; due **Sunday June 6th**).


### Team player/participation (10% of grade)

We will be using a `#problemset` channel in our class Slack for you to ask questions about roadblocks you encounter with the DataCamp activities or on the problem sets. While I will be answering questions within a window of 24 hours, I encourage you to help each other and answer each other's questions. Your participation grade will reflect whether you've helped your classmates on the forum and your participation in class.


