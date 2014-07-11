import sys
import json
import unicodedata

def main():
    # create data dictionairy
    sent_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    tweet_file = open(sys.argv[2])
    tweets = {} # dictionary for all tweets by tweet index
    tweetStates = {} #dictionary of states by tweet index
    tweetindex = 0
    e = 0
    bigscore = 0
    bigindex = 0
    for line in tweet_file:
        tweetindex = tweetindex +1
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    

        tweetState = ''
        tweetscore = 0

        if tweet.get('text','NO') != 'NO': 
            try:
                tweetText = tweet['text']
                tweetText = unicodedata.normalize('NFKD', tweetText).encode('ascii','ignore')
                tweetscore = getTweetScore(tweetText, scores)
                #if tweet.get('place','N__') != 'N__':
                #   state = tweet['place'] ['coordinates']
                #else:
                userLocation = tweet['user']['location']
                userLocation = unicodedata.normalize('NFKD', userLocation).encode('ascii','ignore')
                if len(userLocation) > 0:
                    tokens = userLocation.rsplit(',')
                    if len(tokens) == 2 and len(tokens[1].strip(' ')) == 2:
                        tweetState = tokens[1].strip(' ')
                        # print tweetState
                        
            except UnicodeEncodeError:
                e = e+1
        if tweetscore > bigscore and len(tweetState) > 0:
            bigscore = tweetscore
            bigindex = tweetindex
        tweets[tweetindex] = tweetscore
        tweetStates[tweetindex] = tweetState

    # print winner
    print tweetStates[bigindex]# + ' '+str(bigscore)

    # print maps
    #print str(bigindex) + str(bigscore)
    #print tweets
    #print tweetStates
        

def getTweetScore(twText , scores):
    score = 0;
    tweetTerms = twText.split()
    for item in tweetTerms:
        if scores.get(item, 'NOT FOUND') != 'NOT FOUND':
            score = score + scores[item]
    return score

if __name__ == '__main__':
    main()
