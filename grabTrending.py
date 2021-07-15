import requests

class RedditTrends(object):
    def __init__(self):
        super(RedditTrends, self).__init__()
        
    def getTrends(self):
        r = requests.get("https://www.reddit.com/api/trending_searches_v1.json?gilding_detail=1", headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"})
        if r.status_code == 200:
            return r.json()

if __name__ == "__main__":
    redditAPI = RedditTrends()
    gTrends = redditAPI.getTrends()
    if (not gTrends):
        print("Failed to return trending")
    else:
        for trend in gTrends["trending_searches"]:
            print("""
Name: {}
URL Prefix: {}
Full URL: https://www.reddit.com{}
Author: {}
Upvotes: {}
Number Of Comments: {}""".format(trend["display_string"], trend["results"]["data"]["children"][0]["data"]["subreddit_name_prefixed"], trend["results"]["data"]["children"][0]["data"]["permalink"], trend["results"]["data"]["children"][0]["data"]["author"], trend["results"]["data"]["children"][0]["data"]["ups"], trend["results"]["data"]["children"][0]["data"]["num_comments"]))
