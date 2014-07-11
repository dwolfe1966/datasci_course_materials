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


    # compute scores
    tweet_file = open(sys.argv[2])
    e = 0
    posWordMap = {}
    negWordMap = {}
    for line in tweet_file:
        tweetscore = 0
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('text','NO') != 'NO': 
            try:
                tweetText = tweet['text']
                tweetText = unicodedata.normalize('NFKD', tweetText).encode('ascii','ignore')
                tweetScore = getTweetScore(tweetText, scores)
                if tweetScore != 0:
                    buildWordMap(tweetText,tweetScore, scores, posWordMap, negWordMap)
            except UnicodeEncodeError:
                e = e+1


    # process Word Maps
    for item in posWordMap:
        posCount = posWordMap[item]
        negCount = 0
        if negWordMap.get(item, 'NOT FOUND') != 'NOT FOUND':
            negCount = negWordMap[item]
            del negWordMap[item]
        if negCount == 0:
            negCount = 0.1
        print item+' '+str(posCount/(negCount*1.0))
    # go through terms only in neg word map
    for item in negWordMap:
        negCount = negWordMap[item]
        print item+' '+str(0.1/negCount)
        
def buildWordMap(tweetText,tweetScore, scores, posWordMap, negWordMap):
    tweetTerms = tweetText.split()
    for item in tweetTerms:
        if scores.get(item, 'NOT FOUND') == 'NOT FOUND':
            if tweetScore > 0:
                if posWordMap.get(item, 'NOT FOUND') != 'NOT FOUND':
                    posWordMap[item] = posWordMap[item]+1
                else:
                    posWordMap[item] = 1
            else:
                if negWordMap.get(item, 'NOT FOUND') != 'NOT FOUND':
                    negWordMap[item] = negWordMap[item]+1
                else:
                    negWordMap[item] = 1
           
def getTweetScore(twText , scores):
    score = 0;
    tweetTerms = twText.split()
    for item in tweetTerms:
        if scores.get(item, 'NOT FOUND') != 'NOT FOUND':
            score = score + scores[item]
    return score

if __name__ == '__main__':
    main()
