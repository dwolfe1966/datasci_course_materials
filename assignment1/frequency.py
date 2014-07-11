import sys
import json
import unicodedata

def main():

    # compute # of occurences of each term
    tweet_file = open(sys.argv[1])
    e = 0
    wordMap = {}
    termcount = 0
    for line in tweet_file:
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('text','N') != 'N': 
            try:
                tweetText = tweet['text']
                tweetText = unicodedata.normalize('NFKD', tweetText).encode('ascii','ignore')
                termcount = termcount + buildWordMap(tweetText,wordMap)
            except UnicodeEncodeError:
                e = e+1

    # process Word Maps
    for item in wordMap:
        count = wordMap[item]
        print item+' '+str(count/(termcount*1.0))
    
        
def buildWordMap(tweetText,wordMap):
    tweetTerms = tweetText.split()
    for item in tweetTerms:
        if wordMap.get(item, 'NOT FOUND') != 'NOT FOUND':
            wordMap[item] = wordMap[item]+1
        else:
            wordMap[item] = 1
    return len(tweetTerms)               

if __name__ == '__main__':
    main()
