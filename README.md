# Oil-Well-Decline-Arps-Model-Approach
This program reads well header data and production logs (imported as .csv files) and walks the user through the generation of decline curves for each well provided in the input data. Decline curves are fit with a hyperbolic curve that is estimated using an iterative least squares method.

The Arps model, named after its developer J.J. Arps, is a set of mathematical equations used in oil and gas production forecasting to describe how the production rate of a well declines over time. The Arps model provides three primary decline curve equations: exponential, hyperbolic, and harmonic. Each of these equations is used to represent different types of production decline behaviors observed in real-world oil and gas wells.

The following is an explanation of the Arps decline curve equations and why the hyperbolic curve is often preferred by petroleoum engineers:

1. Exponential Decline (n = 0):
   - The exponential decline curve represents a scenario where the rate of production decline is constant over time.
   - It's suitable for wells that experience a relatively steady decrease in production without significant variations.

2. Hyperbolic Decline (0 < n < 1):
   - The hyperbolic decline curve is one of the most commonly used Arps models because it captures more realistic production decline behavior.
   - It accounts for the fact that production decline tends to slow down over time, which is often observed in oil and gas wells.
   - The hyperbolic curve is characterized by an initial rapid decline in production followed by a slower decline as the well matures.
   - The parameter "n" (often referred to as the "b-factor") determines the curvature of the hyperbolic curve. Values of "n" between 0 and 1 are typically used, with lower values indicating a more pronounced initial decline.

3. **Harmonic Decline (n = 1)**:
   - The harmonic decline curve is used when production decline follows a linear pattern, where the production rate decreases linearly with time.
   - It's less common in practice and is typically used for wells with constant bottom-hole pressure or wells that are under boundary-dominated flow conditions.

The choice of which Arps decline curve to use depends on the characteristics of the well and the observed production behavior. However, in over the years this model has been used, the hyperbolic decline curve is preferred for several reasons:

- Its Realism: The hyperbolic curve reflects the typical behavior of oil and gas wells, where production often experiences an initial rapid decline followed by a slower decline rate as the reservoir pressure decreases.

- Flexibility: The hyperbolic curve allows for a wide range of decline behaviors by adjusting the "b-factor" (n). This flexibility makes it suitable for a variety of well types and conditions.

- Fits Data Well: The hyperbolic model often provides a good fit to real production data, making it a practical choice for forecasting.

- Ease of Interpretation: The parameters of the hyperbolic decline curve (initial rate, "b-factor," and decline rate) are relatively easy to interpret and have physical meaning in the context of well behavior.



### ENVIRONMENT  
**Python 3.12**  
*Required Libraries*  
* sys  
* os  
* numpy  
* pandas  
* matplotlib version 3.8.0  
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

 

