'''
Test primesieve using pi cloud
'''

import time
import timeit
import ConfigParser
import primesieve
import cloud

def get_prime(n):
    return primesieve.get_primes(n)[-1]

def test_picloud(cloud, n, fast):
    begin = time.time()
    jid = cloud.call(get_prime, n, _high_cpu=True)
    cloud.result(jid)
    print n , 
    print "took " ,
    print time.time() - begin , 
    print "seconds"

if __name__ == '__main__':
    # Calculate baseline using Intel Core 2 Duo @ 2.33Ghz 
    
    # Find the 10 millionth prime locally
    t = timeit.Timer("get_prime(10000000)", "from __main__ import get_prime");
    print t.timeit(1) # ~4.6 seconds
    
    # Read in our keys from config file
    config = ConfigParser.ConfigParser()    
    config.read("cloud.config")
    api_key = config.get("PiCloud", "api_key")
    api_secretkey = config.get("PiCloud", "api_secretkey")
    
    cloud.setkey(int(api_key), api_secretkey)
    
    # Regular
    test_picloud(cloud, 100000, False)     # ~2.7s
    test_picloud(cloud, 1000000, False)    # ~1.2s
    test_picloud(cloud, 10000000, False)   # ~3.2s
    test_picloud(cloud, 100000000, False)  # ~22s
    
    # Try high-cpu!
    test_picloud(cloud, 100000, True)     # ~2.7s
    test_picloud(cloud, 1000000, True)    # ~1.2s
    test_picloud(cloud, 10000000, True)   # ~3.2s
    test_picloud(cloud, 100000000, True)  # ~22s
    
   
    