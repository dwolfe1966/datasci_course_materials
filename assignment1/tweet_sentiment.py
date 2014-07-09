import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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
    for line in tweet_file:
        tweetindex = tweetindex +1
        tweetscore = 0
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('text','NO') != 'NO': 
            try:
                tweetTerm = tweet['text']
                tweetscore = getTweetScore(tweetTerm, scores)
                # unneeded
                print tweetTerm
                print 'score='+str(tweetscore)
                print tweet['id_str']
                print tweet['user']['id']
                print tweet['user']['name']
                print '--------------------------'
            except UnicodeEncodeError:
                print "Unicode error" +str(tweetscore)
        else:
            print tweet.items()
        tweets[tweetindex] = tweetscore

    print tweets    
    #hw()
    # lines(sent_file)
    # lines(tweet_file)

def getTweetScore(twText , scores):
    score = 0;
    tweetTerms = twText.split()
    for item in tweetTerms:
        if scores.get(item, 'NOT FOUND') != 'NOT FOUND':
            score = score + scores[item]
    return score

if __name__ == '__main__':
    main()
