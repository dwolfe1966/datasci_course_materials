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
    for line in tweet_file:
        tweet = {} # dictionairy for individual tweet
        tweet = json.loads(line)    
        if tweet.get('text','NO') != 'NO': 
            try:
                print tweet['text']
                print tweet['id_str']
                print tweet['user']['id']
                print tweet['user']['name']
                print '--------------------------'
            except UnicodeEncodeError:
                print "Unicode error"
        else:
            print tweet.items()
        
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
