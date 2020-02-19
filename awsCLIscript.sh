#!/usr/bin/env bash

#aws comprehend batch-detect-dominant-language \
#    --text-list <(grep -Eo '"transcript":.*?[^\\]",' asrOutput.json)


#curl -s 'https://api.github.com/users/lambda' | \
cat ./asrOutput.json | \
    python3 -c "import sys, json; print(json.load(sys.stdin))"
#    python3 -c "import sys, json; print(json.load(sys.stdin)['transcript'])"

#aws comprehend batch-detect-key-phrases \
#    --language-code "en" \
#    --text-list <(grep -Eo '"transcript":.*?[^\\]",' asrOutput.json)



#    --cli-input-json file:/Users/kevinphillips/PycharmProjects/awscomprehend-sentiment-demo/asrOutput.json
#    --generate-cli-skeleton file:/Users/kevinphillips/PycharmProjects/awscomprehend-sentiment-demo/asrOutput.json
#    --generate-cli-skeleton --output
#    --text-list "josh is here"
#    --cli-input-json file:/Users/kevinphillips/PycharmProjects/awscomprehend-sentiment-demo/asrOutput.json #--debug
#    --cli-input-json file:/Users/kevinphillips/PycharmProjects/awscomprehend-sentiment-demo/asrOutput.json
#    --region region
#    --endpoint endpoint
#    --cli-input-json file://path to input file/process.json

