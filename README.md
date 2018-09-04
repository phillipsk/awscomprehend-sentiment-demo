# awscomprehend-sentiment-demo
Demos Sentiment analysis using comprehend batch, document and asynchronous mode


## How to run

### Single doc mode
```bash
export PYTHONPATH=./source
python source/demo.py single "This is great! and amazing"
```


### Batch doc mode
```bash
export PYTHONPATH=./source
python source/demo.py batch tests/data/sample_reviews.csv
```
