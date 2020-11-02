# Calculating a sample variance

We have now been using the flow chart below to perform these hypothesis tests for some time.

![](hypo-testing.003.jpeg)

In all the tests we have performed thus far, however, the null hypothesis has been that the expectation takes a particular value.  In this series of exercises, we are thus going to consider hypothesis tests for investigating whether or not the variance of the distribution is consistent with some model distribution. 

With that in mind, I want to start with a brief revision exercise on calculating the sample variance.  __To complete this task you will need to add code within the function called `sample_variance`__.  This function takes a NumPy array called `data` in input.  It should return the sample variance for the data within the data array, which can be calculated using:

![](https://render.githubusercontent.com/render/math?math=s^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^nX_i^2-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])
