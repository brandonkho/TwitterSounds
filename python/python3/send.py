from OSC import OSCClient, OSCBundle
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


#consumer key, consumer secret, access token, access secret.
ckey="uEMQ6nN20QCDPtGMZGykO6nl6"
csecret="Da0cyc5WlhMnnDys8rZcumYHe6pEpxzxdHaZCvFB52uLkNq0g7"
atoken="4488070093-0dp3AzQXHxdS2qtmVMpQwt9rUfQzspsCXGufUDx"
asecret="ZyCBURfsbDLLCyHAEo93GAtTAMj6L6dByMKwl1JJtxSes"


class listener(StreamListener):

    def on_data(self, data):
        #print(data)
        duration = 0
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            split_tweet = tweet.split(' ')
            first_word = split_tweet[0]
            if first_word == 'RT':
                first_word = split_tweet[1]
            num = 0
            for char in first_word:
                num += ord(char)
            length_of_tweet = len(split_tweet)/40.0
            duration = length_of_tweet * 1000
            #print duration
            sharp_freqs = [185, 207.65, 233.08, 261.63, 277.18, 311.13, 349.23,]
            freqs = [174.61, 196, 220, 246.94, 261.63, 293.66, 329.62, 349.23, ]#369.99, 391.96, 415.30, 440, 466.16, 493.88, 523.25]
            note = num % 7
            freq = 0
            if '#' in tweet:
                freq = sharp_freqs[note]
            else:
                freq = freqs[note]
        except UnicodeEncodeError:
            duration = 500
        
        client = OSCClient()
        client.connect(("localhost", 54345))

        ### Create a bundle:
        bundle = OSCBundle()
        bundle.append({'addr': "/frequency", 'args':[freq]})
        #bundle.append({'addr': "/amplitude", 'args':[52]})
        #bundle.append({'addr': "/envelope/line", 'args:['})
        bundle.append({'addr': "/envelope/line", 'args': [10., 20, 0., duration]})

        client.send(bundle)


        time.sleep(duration/1000)
        
        return(True)

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)



l = listener()
stream = Stream(auth, l)
stream.filter(track=["music"])



