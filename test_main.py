import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sample_var(self) :
        for i in range(5) : 
            tdata = np.random.normal(0,1,size=100)
            mu = sum(tdata) / len(tdata)
            var = (len(tdata) / (len(tdata)-1))*( sum(tdata*tdata) / len(tdata) - mu*mu )
            self.assertTrue( np.abs( var - sample_variance(tdata) )<1e-7, "Your code for calculating the sample variance is not correct" )
