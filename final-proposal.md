 # Final Proposal Specifications

**Purpose**

Micro-Mobility - Small, human or electric-powered transportation market has been on the rise in United States according to Populus report. <a href="https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/micromobilitys-15000-mile-checkup">McKinsey </a> forecasted that micromobility market will be a $200 billion to $300 billion dollar market in United States by 2030. According to the Populus report the few of the factors effecting the new micro-mobility trend are GPS-enabled smartphones apps that make it easier to locate the mobility devices and that in many major U.S.cities it is faster to travel short distance of 3 miles or less using an e-scooter or bike than driving a car or using a ride-hailing service. Many cities are still in the midst of developing policies and regulations to handle the rise in micro-mobility transportation.  The reports highlighties three areas where majority of cities will focus policy and regulations on:

quote

'
1. Ensuring safety: What policies should be enacted to ensure the safety of riders and others using public space (e.g., streets and sidewalks)? What transportation planning and design modifications are possible to promote the safety of those
using shared and personal micro-mobility options and others in the public right
of way?
2. Promoting equitable access to services: Are micro-mobility services accessible, and being utilized, by a broad segment of the population? If not, how can the city support expanding access to disadvantaged populations?
3. Evaluating impacts on traffic and sustainability: How do micro-mobility services fit into the broader transportation ecosystem? Are they reducing vehicle trips? How many micro-mobility vehicles can the residents of a city effectively utilize?

'
end quote

I have met with City of Austin transportation IT staff and they agreed that City of Austin is also focusing on the above policies and is in the process of updating their policies.  



**Format**: Since you will want a public repo at the end of the project, you should create a git repo, 
and your project proposal will be the README.md file in it.

### Directory Structure
* src - directory for all the code
* data - downloaded data (raw and cleaned)
* output - results
* database - database scripts
* documents - documents used for analysis and research

**Length**: Each of the numbered points should have at a few complete sentences to address them. 

**Include the following**:

1. What are you trying to do?  Articulate your objectives using absolutely no jargon (i.e. as if
you were explaining to a salesperson, executive, or recruiter).

City of Austin transportation department updates dockless mobility data they receive from the vendors on their Open Data Portal website every hour. The data contains all the trip information for each dockless mobility device with the exception of trips which meet the following criteria:
- trip distance greater than or equal to .1 miles and less than 500 miles
- trip duration less than 24 hours

For aggregration purposes they created a citywide hexagonal grid with each edge length of 500ft. Each grid is a cell with a unique id. Each trip has origin cell and destination cell id. Few of the important fields in the dataset are :

- ID - Unique trip identifier
- Device ID - Unique ID for the device used to complete the trip
- Vechile Type - Bicycle or Scooter
- Trip Duration - In seconds
- Trip Distance - In meters
- Start Time - Datetime at which the trip started in local time
- End Time - Datetime at which the trip ended in local time
- Origin Cell ID 
- Destination Cell ID
- Start Latitude
- Start Longitude
- End Latitude
- End Longitude 

For full set of fields and description can be found at https://data.austintexas.gov/Transportation-and-Mobility/Dockless-Vehicle-Trips/7d8e-dm7r

My goal is to use this data above and weather data to determine :

1. How does distance traveled, start time of the trips, origin and end point vary by geographical location. For example: Do UT campus trips, Downtown trips and South Congress trip differ by time of the day, distance traveled.
2. Develop a model to predict the number of dockless mobility scooters and usage at give time of the day in a given area (cell). 


2. How has this problem been solved before? If you feel like you are addressing a novel
issue, what similar problems have been solved, and how are you borrowing from those?
I have not come across any prediction models on dockless mobility scooter but found few research papers on Dockless and Docked Bike Sharing prediction models. My goal is to use the following papers for reference:

https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/mobisys16bike.pdf

https://www.researchgate.net/publication/324275044_A_deep_learning_approach_on_short-term_spatiotemporal_distribution_forecasting_of_dockless_bike-sharing_system

3. What is new about your approach, why do you think it will be successful?
My plan is to apply the modeling done in the referenced papers to dockless scooters.

4. Who cares?  If you're successful, what will the impact be?

If successful the model will be presented to City of Austin Transportation Department IT staff which then further might be groups like City of Austin Mobility Committee, City of Austin Compliance Department, AURA to help implement new policies and regulations.

5. How will you present your work?  
  * Web app - where will you host it, what kind of information will you present?
  * Visualization - what final visuals are you aiming to produce?
  * Presentation - slides, interpretive dance?
  
Goal is to present the data through Visualization
  
6. What are your data sources? What is the size of your dataset, and what is your storage format?

   * Dockless Mobility Data - Original Data was downloaded on 2019-02-12 from City of <a href="https://data.austintexas.gov/Transportation-and-Mobility/Dockless-Vehicle-Trips/7d8e-dm7r"> Austin Data Portal  </a>. The downloaded <a href = "https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Dockless_Vehicle_Trips.csv"> data </a> is for trips from 04-03-2018 to 02-12-2019 and is in csv format and is stored on AWS . The current dataset had 2746504 datapoints.
   
   * Austin Bergstorm Airport Weather Data - Daily weather information (temperature, humidity, wind etc.,) recorded at Austin Bergstorm Airport was downloaded from <a href="http://www.ncdc.noaa.gov"> National Oceanic and Atmospheric Adminstration</a> . The data is in <a href="https://s3.amazonaws.com/sameera-bucket-1/dockless_mobility/raw_data/Austin_Bergstom_Airport_Weather.csv"> csv </a> format and has weather informatin 2018-01-01 to 2019-03-12.  The current dataset has 435 datapoints.
   

7. What are potential problems with your capstone, and what have you done to mitigate these problems?
   
   * Since the data is time-series data I have to research time-series prediction algorithms. Apart from my own research my goal is to work with Dan Rupp to get a quick review of time-series analysis and prediction algorithms.
   * Work with City of Austin transportation department to get more insights on grouping of cell IDs to neighborhoods. Determine if there is a mapping file which contains all the cell ids for Downtown Austin, UT campus and South Congress. 


8. What is the next thing you need to work on?
  * Getting the data, not just some, likely all?
    The goal is to work on the downloaded for modeling and use the data from 02-13-2019 to 04-01-2019 for testing the model
  * Understanding the data?
    My initial EDA has revealed few null values in the data so the next steps is to determine ways to handle the null values after determing if the values are MAR, MCAR and MNAR.
  * Building a minimum viable product?
    Do feature extraction and run T-Test on different neighborhoods or cells.
  * Gauging how much signal might be in the data?

**Submission**: Once you are satisfied with your submission, push it to github, and send the repo URL to your
instructors via slack.
