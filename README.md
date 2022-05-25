# Load-Test-and-Spike-Test

This repo is about my last project making Load Test and Spike Test using Jmeter and Locust as load testing tools and for spike test I use Jmeter. Website that I do for this project is https://reqres.in.

## Getting Started

To see report of the load test that I am doing you can see Loadtest Report.docx 

## Prerequisite

To run the tests you need Jmeter, Visual code, locust, python version 3.0 or latest and google chrome to see localhost:8089. This repo works best on Jmeter.

## Running the tests
to run the test on Jmeter here are the steps :

* Open Jmeter

* Click File

* Click Open

* Choose the file from your designated folder 

* Choose ReqresLoadTestandSpikeTest.jmx

to run the test on Locust here are the steps :

* Open Visual Code

* Click File

* Choose Open Folder

* Open new Terminal in your vscode

* In terminal type source venv/Scripts/activate then you can see below the input command there is (venv)

* Then type pip install locust

* Lastly, type locust -f Loadtest/script/loadtest.py

* After those steps you need to open your browser. It work best on chrome browser. Make sure you have one.

## Built With

* [Jmeter](https://katalon.com/) - Load testing software

* [Locust](https://locust.io/) - Load testing framework

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor

## Authors

* Faizal Bayhaque Al Adhanie
