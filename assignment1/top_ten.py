import sys
import json
import unicodedata

def main():

    # compute # of occurences of each term
    tweet_file = open(sys.argv[1])
    e = 0
    hashtagMap = {}
    termcount = 0
    for line in tweet_file:
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('entities','N') != 'N': 
            try:
                entities = tweet['entities']
                if entities.get('hashtags','N') != 'N':
                    hashtags = entities['hashtags']                    
                # tweetText = unicodedata.normalize('NFKD', tweetText).encode('ascii','ignore')
                buildTagMap(hashtags,hashtagMap)
            except UnicodeEncodeError:
                e = e+1

    # process Word Maps
    for item in hashtagMap:
        count = hashtagMap[item]
        item = unicodedata.normalize('NFKD', item).encode('ascii','ignore')
        print item+' '+str(count)
    
        
def buildTagMap(hashtags,hashtagMap):
    for item in hashtags:
        #print item
        itemTag = item['text']
        #print itemTag
        if hashtagMap.get(itemTag, 'NOT FOUND') != 'NOT FOUND':
            hashtagMap[itemTag] = hashtagMap[itemTag]+1
        else:
            hashtagMap[itemTag] = 1
             

if __name__ == '__main__':
    main()
