import numpy as np 


def sample_variance( data ) : 
  # Your code to calculate the sample variance goes here
  
  
# You should not need to modify the code from here onwards.
# It is just here to test that you code for calculating the sample
# variance is working
mydata = np.random.normal(0,1,size=100)
print("The sample variance for the data in mydata is", sample_variance( mydata ) )
