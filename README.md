# Dataset

## Data Acquisition

### StackOverflow dataset
* Use StackOverflow API to get the data here: https://data.stackexchange.com/stackoverflow/query/new
* write the following query

  ```SQL
  SELECT title,concat('https://stackoverflow.com/questions/',id), tags, score, creationDate From Posts
  where body like '%<code>%' and
  tags like '%dataframe%' and tags like '%python%' and score > 9 and
  (body like '%error%' or body like '%bug%' or body like '%not work%' or body like '%fail%' or body like '%performance%' or body like '%expect%' or body like '%crash%' or body like '%incorrect%')
  ```


### Github dataset
* Run the python script to get the json file of the GitHub repositories for a specific package from 2009 to 2020:
  - Run the python script: ``` python get_GH.py```
* Then, for each repository, get all the commits that have word "fix":
  - Run the python script: ```python get_commits.py ```

## R and Python Dataset
GitHub and StackOverflow datasets are in the R and Python folder separately.
