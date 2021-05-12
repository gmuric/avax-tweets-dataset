# Avax tweets dataset
The repository contains two collections associated with vaccine hesitancy on Twitter. The "streaming collection" contains tweets collected by leveraging Twitter streaming API to listen to the set of anti-vaccine keywords. You can see the full list of these keywords in keywords.txt. The "account collection" contains historical tweets of accounts that are susceptible to anti-vaccine narratives. To comply with [Twitter's Terms of Service](https://twitter.com/en/tos), only tweet IDs are released. The data is for non-commercial research purposes only. It is our hope that it will help those who are studying and tracking anti-vaccine misinformation on social media and enable better understanding of vaccine hesitancy.

The associated paper to this repository can be found here: https://arxiv.org/pdf/2105.05134.pdf

## Data Organization
The "streaming-tweetids" folder corresponds to the streaming collection whereas the "account-tweetids" folder corresponds to the account collection. All the files are in .txt format, each containing the list of tweet IDs. Account collection files are named from 0 to 387. Streaming collection files are organized into 7 folders, each corresponds to a month of year 2020 and 2021.

## Notes about the data
1. Only English tweets are considered.
2. The overview of our data collections are summarized below

|   | Streaming collection | Account collection |
| ---- | ---- | ---- |
| Number of tweets      | 1,832,333 | 135,949,773 |
| Number of accounts   | 719,652 | 78,954 |
| Verified accounts      | 9,032 | 239 |
| Average tweets per account   | 2.5 | 1721.8 |
| Accounts with location      | 5,661 | 363 |
| Oldest tweet   | 2010-10-19 | 2007-03-06 |
| Most recent tweet   | 2021-04-21 | 2021-02-02 |


3. You may consider using tools such as the Hydrator, Twarc and tweepy to rehydrate the Tweet IDs. For detailed instructions please see the next section.

4. If you have difficulties accessing some data, please contact the authors: gmuric@isi.edu

## How to Hydrate
### Hydrating using Hydrator (GUI)
Navigate to the Hydrator github repository and follow the instructions for installation in their README. As there are a lot of separate Tweet ID files in this repository, it might be advisable to first merge files from timeframes of interest into a larger file before hydrating the Tweets through the GUI.

### Hydrating using Twarc (CLI)
Many thanks to Ed Summers (edsu) for writing this script that uses Twarc to hydrate all Tweet-IDs stored in their corresponding folders.

First install Twarc and tqdm
```
pip3 install twarc
pip3 install tqdm
```

Configure Twarc with your Twitter API tokens (note you must apply for a Twitter developer account first in order to obtain the needed tokens). You can also configure the API tokens in the script, if unable to configure through CLI.
```
twarc configure
```
Run the script. The hydrated Tweets will be stored in the same folder as the Tweet-ID file, and is saved as a compressed jsonl file
```
python3 hydrate.py
```
### Hydrating using Tweepy:
```
import tweepy
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, retry_count=5, retry_delay=2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
api.statuses_lookup(list_of_ids) #consider the limitations in tweepy documentation

```
# Data Usage Agreement / How to Cite
By using this dataset, you agree to remain in compliance with [Twitter's Term of Service](https://twitter.com/en/tos), and cite the following manuscript:
Muric G, Wu Y, Ferrara E. COVID-19 Vaccine Hesitancy on Social Media: Building a Public Twitter Dataset of Anti-vaccine Content, Vaccine Misinformation and Conspiracies, arXiv:2105.05134 [cs.SI] 2021.

```
@article{Muric2021,
archivePrefix = {arXiv},
arxivId = {2105.05134},
author = {Muric, Goran and Wu, Yusong and Ferrara, Emilio},
eprint = {2105.05134},
month = {may},
title = {{COVID-19 Vaccine Hesitancy on Social Media: Building a Public Twitter Dataset of Anti-vaccine Content, Vaccine Misinformation and Conspiracies}},
url = {http://arxiv.org/abs/2105.05134},
year = {2021}
}
```

