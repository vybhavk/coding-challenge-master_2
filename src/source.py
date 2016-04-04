# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:22:29 2016

@author: anuragreddygaddamvenakat


"""
### class code
import unicodedata as sys, os, simplejson
import pandas as pd
sys.argv[1] 
twitter_input = sys.argv[2]
output_file=sys.argv[3]
#unique_tags=[]
total_time = []
total_hash = []
def inputfile(twitter_input):
    
    for line in twitter_input:        
        single_tweet = simplejson.loads(line)
        if 'created_at'in single_tweet:            
            if(len(single_tweet["entities"]['hashtags'])>0):
                tags=[]
                time_stamp = single_tweet['created_at']                
                hash_tags = single_tweet["entities"]['hashtags']
                total_time.append(time_stamp)
                for i in range(len(hash_tags)):
                    tags.append(hash_tags[i]["text"])
                total_hash.append(tags) 
                
    return (total_time,total_hash)
#df.sort(['c1','c2'], ascending=False)
data=pd.DataFrame(columns=('Time_stamp','Hashtags'))
# calling the inputfile function to get the data to the dataFrame
data.Time_stamp,data.Hashtags=inputfile(twitter_input)
# converting to the time stamp format 
data.Time_stamp=pd.to_datetime(data.Time_stamp)
data=data.sort_values('Time_stamp')
#data = data.sort(['Time_stamp'], ascending=True)
#data.set_index[[range(0,data.shape[0])]]
data.index = range(0,data.shape[0])
data.to_csv("/Users/anuragreddygaddamvenakat/Downloads/coding-challenge-master/data-gen/test.csv")
def avg_score(score_val):
        
    
    return((score_val)/float(len(unique_tags)))
    
# Class to calculate score of a tweet
class Calculate_score(object):
    
    """ 
    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, time,tags):
        
        #time = temp2.Time_stamp[0]
        #tags = temp2.Hashtags[0]
        """Return the time with respective to the tags""" 
        self.time = time
        #print time
        self.tags = tags
        #print self.tags
        self.length=len(tags)
        #self.scores=0
        self.new_tags=[]
        #print self.new_tags
# assigning the new elements to unique tags
        global unique_tags 
        self.new_tags = list(set(tags)-set(unique_tags))
        #print unique_tags
        #print self.new_tags
        if self.length != 1:
            unique_tags = unique_tags+self.new_tags
        self.newtags_length=len(self.new_tags)
                
  
# generating scores        
    def score(self):
        self.scores=(self.length-1)*(self.newtags_length)+(self.newtags_length)*(self.length-self.newtags_length)   
        #print self.scores
        return (self.scores)
        
        
    def write_file(score_val):
        with open(output_file,'a') as f:
        #print avg_score(score_val)
            f.write("{}\n".format((score_val)))
     
prev_avg_score = []
unique_tags = []
from datetime import timedelta
#for j in range(data.shape[0]):
temp1 = pd.DataFrame(columns=('Time_stamp','Hashtags'))
score_val = 0
for j in range(data.shape[0]):
    print j
    #unique_tags =[]
    End_tag=data.Time_stamp[j]
    Start = End_tag - timedelta(seconds=60)
    #print "Start" 
    #print Start
    #print "End"
    #print End_tag
    temp1 = temp1.append(data.loc[j])
    #print 'tags with in 60s from the first'
    #temp2= temp1[(temp1['Time_stamp']>Start)&(temp1['Time_stamp']<=End_tag)]
    temp2= temp1[(temp1['Time_stamp']>Start) & (temp1['Time_stamp']<=End_tag)]
    if((temp1.shape[0]-temp2.shape[0])>0):
       unique_tags = []
       score_val=0
    temp2.index = range(0,temp2.shape[0])
    

                 #temp.head()
    #temp['score'] = 0
    #temp.loc[:,('score')]=''
    
    for i in range(temp2.shape[0]):
        #print 'tweet tags'
        #print i
        #print temp2.Hashtags[i]
        a=Calculate_score(temp2.Time_stamp[i],temp2.Hashtags[i])
        score_val = a.score() + score_val
        #temp.loc[i,['score']]=a.score()
        #print'printing unique tags '
        #print unique_tags
        #print 'score'
        #print score_val
       # print 'avg score'
    
    if (len(unique_tags) == 0):
        print prev_avg_score
        print 'success'
        write_file(round(prev_avg_score,2))  
    else:
        print avg_score(score_val) 
        prev_avg_score = avg_score(score_val)
        print 'nsuccess'
        write_file(round(prev_avg_score,2))
    
       