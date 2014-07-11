import sys
import json


def main():
    # create data dictionairy
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    tweet_file = open(sys.argv[2])
    tweets = {} # dictionary for all tweets
    tweetindex = 0
    e = 0
    for line in tweet_file:
        tweetindex = tweetindex +1
        tweetscore = 0
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('text','NO') != 'NO': 
            try:
                tweetText = tweet['text']
                tweetscore = getTweetScore(tweetText, scores)
                # unneeded
                #print tweetText
                #print 'score='+str(tweetscore)
                #print tweet['id_str']
                #print tweet['user']['id']
                #print tweet['user']['name']
                #print '--------------------------'
            except UnicodeEncodeError:
                e = e+1
                #print "Unicode error" +str(tweetscore)
        #else:
            #print tweet.items()
        tweets[tweetindex] = tweetscore
        print tweetscore
        

def getTweetScore(twText , scores):
    score = 0;
    tweetTerms = twText.split()
    for item in tweetTerms:
        if scores.get(item, 'NOT FOUND') != 'NOT FOUND':
            score = score + scores[item]
    return score

if __name__ == '__main__':
    main()
