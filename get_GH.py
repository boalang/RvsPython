#!/usr/bin/python


import urllib.request, json
import time
import  sys
import os
import json
import glob


def get_package(pkg, year):

    data = ""

    for j in range(1, 13):
        url = ''
        mins = 0
        while mins < 3:
            for i in range(mins * 10 + 1, mins * 10 + 11):

                if i < 10 and j < 10:
                    url = 'https://api.github.com/search/repositories?q=' + pkg +'+language:r+created:'+ year +'-0' + str(
                        j) + '-0' + str(i) + "&per_page=100"

                if i < 10 and j >= 10:
                    url = 'https://api.github.com/search/repositories?q=' + pkg +'+language:r+created:'+ year +'-' + str(
                        j) + '-0' + str(i) + "&per_page=100"

                if i >= 10 and j < 10:
                    url = 'https://api.github.com/search/repositories?q=' + pkg +'+language:r+created:'+ year +'-0' + str(
                        j) + '-' + str(i) + "&per_page=100"

                if i >= 10 and j >= 10:
                    url = 'https://api.github.com/search/repositories?q=' + pkg +'+language:r+created:'+ year +'-' + str(
                        j) + '-' + str(i) + "&per_page=100"

                try:
                    with urllib.request.urlopen(url) as url1:
                        data = json.loads(url1.read().decode())
                except Exception as e:
                    print(e)

                try:
                    with open(pkg + "_" +  year + str(j) + '_' + str(i) + ".json", "w+") as outfile:
                        json.dump(data, outfile)
                except Exception as e:
                    print(e)
            time.sleep(30)
            mins += 1


def get_repos():
    files_list = glob.glob("*.json")

    for i in range(len(files_list)):
        with open(files_list[i], "r") as json_file:
            data = json.load(json_file)
            try:
                repos_dic = data['items']

                with open("repos_list", "a") as outFile:
                    for i in range(len(repos_dic)):
                        outFile.write(repos_dic[i]['full_name'] + "\n")
            except:
                print("Error in getting items")



def get_commits():
    array = []
    with open("repos_list", "r") as reps_file:
        for line in reps_file:
            array.append(line.strip())

    count = 0
    for j in range(1, len(array)):
        count = count + 1

        os.system(
            'curl -H "Accept: application/vnd.github.cloak-preview"' + ' -s https://api.github.com/search/commits?q=repo:' + str(
                array[j]) + '+fix > ' + str(j) + '.json')
        if count % 10 == 0:
            time.sleep(30)


def get_commits_urls():
    files_list = glob.glob("*.json")

    for i in range(len(files_list)):
        with open(files_list[i], "r") as json_file:
            data = json.load(json_file)

            try:
                repos_dic = data['items']

                with open("commits_list", "a") as outFile:
                    for i in range(len(repos_dic)):
                        outFile.write(repos_dic[i]['html_url'] + "\n")
            except:
                print("error in getting data items")


# Step 1
for i in range (2009,2020):
   get_package("data.table", str(i))
get_repos()


# Step 2: Move all the json files based on the year and package name to other location on your disk

# Step 3 get the commits URL
# Stop for 15 min

get_commits()
get_commits_urls()
