import re

def calculate_profanity(tweet, racial_slurs):
   
    tweet = tweet.lower()
    tweet = re.sub(r'[^\w\s]', '', tweet)  # remove all non-word characters
    words = tweet.split()
    num_slurs = len([word for word in words if word in racial_slurs])
    return num_slurs / len(words)

def main():
   
    with open('racial_slurs.txt', 'r') as f:
        racial_slurs = set([line.strip() for line in f])
    with open('tweets.txt', 'r') as f:
        tweets = [line.strip() for line in f]
    for tweet in tweets:
        profanity = calculate_profanity(tweet, racial_slurs)
        print(f'{tweet}: {profanity}')

if __name__ == '__main__':
    main()