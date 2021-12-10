# SentimentAnalysis
Dockerized Sentiment Analysis Project 

## I - THE ML MODEL

	- Find a dataset on which we can perform sentiment analysis (Eventually need webscraping)
	- Cleaning datasets 
	- Creating NLP model for sentiment analysis as multi-class classification (pos/neg/neutral)
	- Training model with pre-processed data
	- Testing model accuracy
    - Unit
    
Output : Model ready & pre-trained, with 80% accuracy minimum.

## II - The Web Interface 

    - Flask web app technology 
    - Text input where an user can add a sentence into it
    - Submit button
    - Output : Positive/Negative/neutral

Output : Running application where an end user can access through a web browser and start using it immediately.

## III - The application package

    - Docker image 
        - Creating Dockerfile ( don't forget port )
        - Adding requirements.txt file
        - Dockerizing an image of the project.

Output : Running the app through the container on any user computer.


## Starting the Web App localy

 Go in *web_app* folder and tap this command :

 ```
uvicorn app:app --reload
 ```

 To see the prediction form, go to this adress :

 **http://127.0.0.1:8000/form**