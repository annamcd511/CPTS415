#!/usr/bin/env python
from mrjob.job import MRJob

class bird_stats(MRJob):

    def mapper(self, _, line):

        _, bird, latitude,longitude,date = line.split(',') #getting data
        
        if (bird =="COMMON NAME"): #ensures to not use the header
            return
        else: 
            year = date[:4] #getting rid of the time information
            yield (year,latitude,longitude),1
  
    def reducer(self, key, values):
        yield key, (sum(values))


if __name__ == '__main__':
    bird_stats.run()