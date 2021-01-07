import os
import time
import json
array = []
with open("repos_list", "r") as reps_file:
    for line in reps_file:
        array.append(line.strip())

count = 0
for j in range(1, len(array)):
    count = count + 1

    os.system(
        'curl -H "Accept: application/vnd.github.cloak-preview"' + ' -s https://api.github.com/search/commits?q=repo:' + str(array[j]) + '+fix > ' + str(j) + '.json')
    if count % 10 == 0:
        time.sleep(60)
        