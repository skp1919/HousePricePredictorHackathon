Problem Statement 1: CredScore Application
Group Name: Week 6 Hackathon : Group 15

## File components
- static : This is a folder to store all static assets like javascripts, css, images
    - main.css : This is a css file to style the web application
    - explain.svg :  decision tree visualization saved in svg format
- templates : This is a folder to store the html templates to render UI
    - layout.html : The common layout page for all web pages in the application
    - predict.html : This is the page to hold the Predictor form
    - result.html : This is the page to show the results
- main.py : This is the main python file for the api application.
- ml_utils.py : This is the utility file to perform the actual ml processing like data loading, model building, training, predicting
- test_app.py : This is to test the api methods
- ci_cd.yaml : This is configuration file to setup workflow for ci cd
- mainweb.py : This is the main python file for web application.
- credit_score_form.py: This is the file to have the credit score form which is loaded into predict html
- requirements.txt : This lists all the dependencies
- screenshots : This sfolder has the screenshots.
- Tester.ipynb : jupyter notebook file used to test, before adding them to actual project
- credit_data_actual_values.py : Helper file to substitue actual values
- ReadMe.md: This is the read me file.


## Running Instructions
- Install dependencies using `pip3 install -r requirements.txt`
- Run api application using `python main.py`.
- Run web application using `python mainweb.py`
- We can do predict using api or launching web app UI. Screenshots available will help.
- To run tests use `pytest`

## CI/CD
- `build` (test) for all the pull requests
- `build` (test) and `upload_zip` for all pushes


Note: This is checked into github : https://github.com/skp1919/week6hackathongroup15/tree/master