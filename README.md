# IPL Match Outcome Prediction

![IPL00](/IPL00.png)
![IPL01](/IPL01.png)
![IPL02](/IPL02.png)
![IPL03](/IPL03.png)

## Overview

This project aims to predict the outcome of Indian Premier League (IPL) cricket matches using machine learning models. The dataset includes match and delivery details from previous IPL seasons.

## Project Structure

- `data/`: Contains the dataset files (`deliveries.csv`, `matches.csv`).
- `scaler_data.pkl`: Pickle file containing mean and standard deviation for feature scaling.
- `model_ann2048_dp.h5`: Trained ANN model with 2048 nodes and dropout.

## Data Preprocessing

- Handle missing values in matches dataset.
- Fill NaN values in relevant columns.
- Normalize team names and clean data for frequent teams.

## Feature Engineering

- Calculate cumulative runs by ball for each inning and match.
- Evaluate current run rate, total balls delivered, balls left, and wicket fall.

## Exploratory Data Analysis

- Analyze leading runs scorers and wicket-takers.
- Visualize most wins by teams.
- Explore top performers in different aspects of the game.

## Finalized Data and Variables

### Data Selection

The dataset used for this project consists of two main files:
- `deliveries.csv`: Contains details about each ball delivered in IPL matches.
- `matches.csv`: Provides information about each match, including teams, venue, outcome, and player of the match.

### Data Cleaning and Preprocessing

1. **Handling Missing Values:**
   - Identify and handle missing values in both `deliveries.csv` and `matches.csv`.
   - Fill NaN values in relevant columns with appropriate substitutions.

2. **Normalization of Team Names:**
   - Normalize team names to ensure consistency.
   - Combine variations of team names (e.g., "Deccan Chargers" to "Sunrisers Hyderabad").

3. **Discarding Non-Frequent Teams:**
   - Identify and discard matches involving non-frequent teams.
   - Filter out deliveries corresponding to the selected matches.

### Selected Variables

The final dataset for model training and prediction includes the following variables:

- `batting_team`: Encoded label for the batting team.
- `bowling_team`: Encoded label for the bowling team.
- `run_scored`: Total runs scored in the inning.
- `curr_run_rate`: Current run rate calculated during the match.
- `target`: Target score set by the batting team.
- `wickets_left`: Number of wickets yet to fall.
- `Req_run_rate`: Required run rate for the batting team.
- `runs_left`: Number of runs needed to win.

These variables provide crucial information about the match dynamics and are used to predict the outcome of the match (win/loss) in the second inning.

### Feature Selection

The following features were selected for model training:

- `batting_team`
- `bowling_team`
- `run_scored`
- `curr_run_rate`
- `target`
- `wickets_left`
- `Req_run_rate`
- `runs_left`

### Feature Scaling

To ensure consistent scales across features, the data was standardized using `StandardScaler`. The mean and standard deviation used for scaling were saved in the `scaler_data.pkl` file for future use.

## Model Training

- Train Random Forest, Logistic Regression, Decision Tree, and KNN models.
- Evaluate models using k-fold cross-validation.

## Model Comparison

- Compare model performance on training and test datasets.
- Visualize metrics such as accuracy and root mean squared error.

## Neural Network Model (ANN)

- Implement and tune an Artificial Neural Network (ANN) for prediction.
- Visualize training and validation loss and accuracy.

## Hyperparameter Tuning

- Experiment with different configurations of the ANN model.
- Select the model with optimal hyperparameters.

#### ANN Model with 256 as maximum number of nodes
- We see that tere is irregularity in loss and accuracy for test data.
- The model has low steepness, this may take large number of epochs to reach better result.

![256](/256.png)

#### ANN Model with 512 as maximum number of nodes
- Still the problem continues.
![512](/512.png)

#### ANN Model with 1024 as maximum number of nodes
- The model is still not performing well.
![1024](/1024.png)

#### ANN Model with 2048 as maximum number of nodes
- The model is performing well.
![2048](/2048.png)

#### ANN Model with 2048 as maximum number of nodes and some Dropouts 0f 0.2
- To overcome overfitting we introduce dropouts.
- This model gives best result and least value of loss.
![2048-0.2](/2048-0.2.png)

## Model Deployment

- Save the final ANN model for future predictions.

## Conclusion

The ANN model with 2048 nodes and dropout layers demonstrated the best performance in predicting IPL match outcomes. The model has been saved for deployment and future use.

![model](/2048-0.2.png)


