# Oil-Well-Decline-Arps-Model-Approach
This program reads well header data and production logs (exported from Drilling Info as .csv files) and walks the user through the generation of decline curves for each well provided in the input data. Decline curves are fit with a hyperbolic curve that is estimated using an iterative least squares method.

### ENVIRONMENT  
**Python 3.12**  
*Required Libraries*  
* sys  
* os  
* numpy  
* pandas  
* matplotlib version 1.5.3  
* mpl_toolkits.basemap  
  
## 0.0 Provide .csv of Well production data and .csv of well header data
Examples in `./data` 
prepare data by deleting all the commas from the values in the 'Well production data' and 'well header data' files
This can be done easily in excel with find-and-replace.  
  
## 1.0 Select wells based on critieria available in well data  
Follow the prompts after starting program  
  
## 2.0 Compute type curve  
Based on https://www.uky.edu/KGS/emsweb/devsh/production/decline_obj.py  
  
## 3.0 plot type curve  
Results are saved to `./results`  

 

