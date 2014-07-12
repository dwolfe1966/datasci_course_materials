import sys
import json
import unicodedata

def main():

    # compute # of occurences of each term
    tweet_file = open(sys.argv[1])
    hashtagMap = {}
    for line in tweet_file:
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)   
        # hunt for hashtags 
        huntForHashTags(tweet, hashtagMap)     
        
    # process Word Maps
    i = 0
    for item in hashtagMap:
        i = i+1
        count = hashtagMap[item]
        if i < 11:
            print item+' '+str(count)

def huntForHashTags(tweet, hashtagMap):
    e = 0
    if tweet.get('entities','N') != 'N': 
        try:
            entities = tweet['entities']
            if entities.get('hashtags','N') != 'N':
                hashtags = entities['hashtags']                    
                buildTagMap(hashtags,hashtagMap)
        except UnicodeEncodeError:
            e = e+1
                
    if tweet.get('user','N') != 'N': 
        try:
            user = tweet['user']
            if user.get('hashtags','N') != 'N':
                hashtags = user['hashtags']                    
                buildTagMap(hashtags,hashtagMap)
            if user.get('entities','N') != 'N':
                entities = user['entities']
                if entities.get('hashtags','N') != 'N':
                    hashtags = entities['hashtags']                    
                    buildTagMap(hashtags,hashtagMap)
            if user.get('status','N') != 'N':
                status = user['status']
                if status.get('entities','N') != 'N':
                    entities = status['entities']
                    if entities.get('hashtags','N') != 'N':
                        hashtags = entities['hashtags']                    
                        buildTagMap(hashtags,hashtagMap)
        except UnicodeEncodeError:
            e = e+1

        
def buildTagMap(hashtags,hashtagMap):
    for item in hashtags:
        itemTag = item['text']
        itemTag = unicodedata.normalize('NFKD', itemTag ).encode('ascii','ignore')
        if hashtagMap.get(itemTag, 'NOT FOUND') != 'NOT FOUND':
            hashtagMap[itemTag] = hashtagMap[itemTag]+1
        else:
            hashtagMap[itemTag] = 1
             

if __name__ == '__main__':
    main()
