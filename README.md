# machine-learning-rent-prediction

<p align="center"><img src="https://cdn-icons-png.flaticon.com/512/2464/2464176.png" alt="mach-learn" width="25%" border="0"><br /></p>


<h1 align="center"> 🧮 Machine learning | Rent prediction </h1>

## Project Status
<p>:heavy_check_mark: Complete<p>

## Table of Contents 
- [Objective](#objective)
- [Process](#Process)
- [Results](#Results)
- [Authors](#Authors)

## Objective
For this project the objective is to create a machine learning solution to predict the average rent in the city of São Paulo. Alongside with the prediction, an API will be built to serve the model.

## Process
 - Explore the data
 - Clean the data
 - Create the model
 - API building

## Data exploration
Here it was imported the data containing all the information about renting in major cities of Brazil. In order to explore and build a robust model, it was decided to work on top of only São Paulo data. To better visualize the data it was built graphs that would aid finding outliers and bad data.

## Data treatment
For this section it was removed any unwanted columns, outliers and bad data. Also it was established a correlation graph to verify which features present the most impact when it comes to rent price.
<p align="center"><img src="images/graphs.PNG" alt="graphs" border="0"><br /></p>

## Model creation
Using the <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html" target="blank"> random forest regressor from scikit-learn </a> as the prediction model, it was possible to train the data and compare the results to the actual sample. After the model was built, using <a href="https://joblib.readthedocs.io/en/latest/" target="blank"> joblib </a> it was exported to be further implemented in an API.

## API building
The API was built using a combination of a remote server instantiated by Flask and a connection to said API on jupyter notebook. After the connection to the API was established, by passing in the parameters to the URL, the model would predict that rent value as an output. After the prediction was made, the operation was stored in a database, created using the aid of <a href="https://www.sqlite.org/index.html" target="blank"> SQlite </a> library.

## Results
With the connection to the API established, by tweaking the parameters in the connection the output is presented simultaneously in jupyter notebook and in the remote server, accessed by the local server URL. 
<p align="center"><img src="images/API_connection.PNG" alt="API_connection" border="0"><br /></p>
<p align="center"><img src="images/API_output.PNG" alt="API_output" border="0"><br /></p>

## Authors
<p>Jonas Angulski <p>

<p> Source: <a href="https://www.dataviking.com.br/trilhamachinelearning" target="_blank"> https://www.dataviking.com.br/trilhamachinelearning </a>

<p> Special thanks to <a href="https://www.linkedin.com/in/tedpetrou/" target="blank"> Odemir Depieri Jr. </a> for instructing this course.