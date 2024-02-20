import pandas as pd
import json

path = 'RC_2007-10'
save_file_authors = 'authors.json'
save_file_subreddits = 'subreddits.json'

# Read the data into a DataFrame
# We have to keep in mind that every line is a different json object
# So we have to read the file line by line

df = pd.read_json(path, lines=True)

authors = df['author'].unique()
subreddits = df['subreddit'].unique()

print('There are {} unique authors'.format(len(authors)))
print('There are {} unique subreddits'.format(len(subreddits)))

# Save the authors to a json file

with open('pandas_' + save_file_authors, 'w') as f:
    json.dump(authors.tolist(), f)

# Save the subreddits to a json file

with open('pandas_' + save_file_subreddits, 'w') as f:
    json.dump(subreddits.tolist(), f)

# Now we need to repeat the process manually

jsons = []

with open(path, 'r') as f:
    for line in f:
        jsons.append(json.loads(line))

authors = set()
subreddits = set()

for sub_json in jsons:
    authors.add(sub_json['author'])
    subreddits.add(sub_json['subreddit'])

print('There are {} unique authors'.format(len(authors)))
print('There are {} unique subreddits'.format(len(subreddits)))

# Save the authors to a json file

with open('manual_' + save_file_authors, 'w') as f:
    json.dump(list(authors), f)

# Save the subreddits to a json file

with open('manual_' + save_file_subreddits, 'w') as f:
    json.dump(list(subreddits), f)