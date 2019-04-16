# Dockless Scooter Rides Prediction
Predict the number of scooter rides originating in a region(cell) in City of Austin


### Business Understanding

Micro-Mobility - Small, human or electric-powered transportation market forecasted by McKinsey report to be $200 - $300 billion dollar market by 2030 in United States alone has been on the rise. One of the main reason for this rise is attributed to the fact that traveling a short distance of 3 miles or less in many major U.S.cities is faster through e-scooters or bikes than driving a car or using a ride-sharing service. Because of the quick rise in trends and market share many cities are still in the midst of developing policies and regulations. Populus report highlighties three areas where majority of cities will focus policy and regulations on:

 > 1. Ensuring safety: What policies should be enacted to ensure the safety of riders and others using public space (e.g., streets and sidewalks)? What transportation planning and design modifications are possible to promote the safety of those
 using shared and personal micro-mobility options and others in the public right
 of way?
 > 2. Promoting equitable access to services: Are micro-mobility services accessible, and being utilized, by a broad segment of the population? If not, how can the city support expanding access to disadvantaged populations?
 > 3. Evaluating impacts on traffic and sustainability: How do micro-mobility services fit into the broader transportation ecosystem? Are they reducing vehicle trips? How many micro-mobility vehicles can the residents of a city effectively utilize?

  City of Austin transportation IT staff agree that City of Austin is also focusing on the above policies and is in the process of updating their current policies to incorporate new findings from different interest groups, studies and citizen feedback. My goal is to present my analysis to the City of Austin transportation department so they can then present to groups working on Micro-mobility policy and regulations.

### Technology Stack
<img src="documents/images/technology_stack.png"
     alt="Technology Stack"
     style="float: left; margin-right: 10px;" />

### Directory Structure
    * src - directory for all the code
    * data - downloaded data (raw and cleaned)
    * output - results
    * documents - documents used for analysis and research
    
### Data Sources
City of Austin Open Data Portal Dockless Mobility Data 
Daily Weather from National Centers for Environmental Information (NCEI) - Austin Bergstrom Airport Weather Station

#### Data Format

City of Austin transportation department updates their dockless mobility data every hour on their Open Data Portal. For aggregration purposes they created a citywide hexagonal grid(cell) with each edge of grid of length 500ft. Each grid is a cell with a unique id. Each trip has origin cell and destination cell id. Few of the important fields in the dataset :

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

 Full set of fields and description can be found at https://data.austintexas.gov/Transportation-and-Mobility/Dockless-Vehicle-Trips/7d8e-dm7r
   
   
   

### Exploratory Data Analysis

### Hypothesis Testing

### Predictive Modeling

### Results

### Future Work
 

### Acknowledgments
  City of Austin Transportation Department  
  Galvanize Instructors and Classmates of Galvanize Jan 2019 Cohort

### References
<a href = "documents/Populus_MicroMobility_2018_Jul.pdf">Populus Report</a>  
<a href="https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/micromobilitys-15000-mile-checkup">McKinsey Report</a>  
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/mobisys16bike.pdf  
https://www.researchgate.net/publication/324275044_A_deep_learning_approach_on_short-term_spatiotemporal_distribution_forecasting_of_dockless_bike-sharing_system


