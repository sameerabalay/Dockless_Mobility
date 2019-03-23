 # Final Proposal Specifications

**Purpose**: Begin to organize actual capstone project.

**Format**: Since you will want a public repo at the end of the project, you should create a git repo, 
and your project proposal will be the README.md file in it.

### Directory Structure
* src - directory for all the code
* data - downloaded data (raw and cleaned)
* output - results
* database - database scripts

**Length**: Each of the numbered points should have at a few complete sentences to address them. 

**Include the following**:

1. What are you trying to do?  Articulate your objectives using absolutely no jargon (i.e. as if
you were explaining to a salesperson, executive, or recruiter).
- What kind of trips are dockless vehicles replacing? Cars/rideshare? Bicycles? Bike Share? Walking? Transit?
- How do trip patterns/behaviors vary geographically? E.g. are campus trips vs downtown trips vs south congress trips distinct in some way? (Distance, time, origins?)

2. How has this problem been solved before? If you feel like you are addressing a novel
issue, what similar problems have been solved, and how are you borrowing from those?
I currently have any not found any prediction algorithms on Dockless Mobility Scooters. I found few research papers on Dockless and Docked Bike Sharing. I'm using the following papers as
reference

https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/mobisys16bike.pdf

https://www.researchgate.net/publication/324275044_A_deep_learning_approach_on_short-term_spatiotemporal_distribution_forecasting_of_dockless_bike-sharing_system

3. What is new about your approach, why do you think it will be successful?
The plan is to apply the ideas from bike sharing systems to Dockless Scooter Data. 

4. Who cares?  If you're successful, what will the impact be?

If successful the model will be presented to City of Austin Transportation Department IT staff which they might further present the findings to groups like City of Austin Mobility Committee, City of Austin Compliance Department, AURA 

5. How will you present your work?  
  * Web app - where will you host it, what kind of information will you present?
  * Visualization - what final visuals are you aiming to produce?
  * Presentation - slides, interpretive dance?
  
  Goal is to present the data through Visualization
  
6. What are your data sources? What is the size of your dataset, and what is your storage format?

   * Dockless Mobility Data - 2746504 datapoints. <a href = "https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Dockless_Vehicle_Trips.csv">City of Austin Dockless Vechicle Trip Data from  2018-04-03 to 2019-02-12
   </a>. Original Data was downloaded on 2019-02-12 from City of <a href="https://data.austintexas.gov/Transportation-and-Mobility/Dockless-Vehicle-Trips/7d8e-dm7r"> Austin Data Portal  </a>
   
   
   * Austin Bergstorm Airport Weather Data - 435 datapoints. Daily weather information at Austin Bergstorm Airport from <a href="https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Bergstom_Airport_Weather.csv"> 2018-01-01 to 2019-03-12 </a>. Original Data was downloaded from <a href="http://www.ncdc.noaa.gov">National Oceanic and Atmospheric Adminstration</a>      
   

7. What are potential problems with your capstone, and what have you done to mitigate these problems?

8. What is the next thing you need to work on?
  * Getting the data, not just some, likely all?
  * Understanding the data?
  * Building a minimum viable product?
  * Gauging how much signal might be in the data?

**Submission**: Once you are satisfied with your submission, push it to github, and send the repo URL to your
instructors via slack.
