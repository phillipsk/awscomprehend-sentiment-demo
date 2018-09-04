# awscomprehend-sentiment-demo
Demos Sentiment analysis using comprehend batch, document and asynchronous mode

## Prerequisites
1. Python 3.5+, https://www.python.org/downloads/release/python-350/ 
2. Install pip, see https://pip.pypa.io/en/stable/installing/ 
3. Install dependencies for this project
```bash
pip install -r source/requirements.txt
``` 

## How to run
### Single doc mode
```bash
export PYTHONPATH=./source
python source/demo.py single "This is great! and amazing"
```


### Batch doc mode
```bash
export PYTHONPATH=./source
python source/demo.py batch tests/data/sample_reviews.csv --outfile /tmp/sentiment.csv
```
