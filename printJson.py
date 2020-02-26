import json, sys

# print(json.load(sys.path())['transcript'])

with open('./asrOutput.json', "r") as f:
    data = json.load(f)
    # print(json.dumps(data, indent=4, sort_keys=True))
    # array = json.load(f)
# print(array)

# import sys, json; print(json.load(sys.stdin)['transcript'])
# //load the data into an element
# data = json.load(f)

# //dumps the json object into an element
json_str = json.dumps(data)

# //load the json to a string
resp = json.loads(json_str)

respB = resp['results']
respC = respB['transcripts']
respD = respC[0]
respE = respD['transcript']
# //print the resp
# print (resp)

# //extract an element in the response
# print(respC)
# print(json.dumps(respC, indent=4, sort_keys=True))

print(respE)

res = len(respE.split())
lines = respE.split(".")

# printing result
print("The number of words in string are : " + str(res))

filename = "./TXT_asrOutput.txt"
with open(filename, 'w') as w:
    for line in lines:
        w.write(line + '\n')
#
#     with open(filename) as f:
# for line_data in sorted_lines:
#     line = '[' + str(datetime.timedelta(seconds=int(round(float(line_data['time']))))) + '] ' + line_data.get(
#         'speaker') + ': ' + line_data.get('line')
#     w.write(line + '\n\n')