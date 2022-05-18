#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# ### Mean: The average of values

# In[2]:


def mean(*args):
    val_sum = sum(args)
    return val_sum /len(args)
print(f'Mean : {mean(1,2,3,4,5)}')


# In[3]:


def mean_for_lists(lista):
    val_sum = sum(lista)
    return val_sum /len(lista)


# In[4]:


mean_list1 = [32, 56, 99, 83, 24]

print(f'Mean : {mean_for_lists([1,2,3,4,5])}')
print(f'Mean : {mean_for_lists(mean_list1)}')

# print(mean(mean_list1)) <-- results in TypeError


# ### Median: the middle number in a numerically-sorted odd dataset
# ### or the average of the 2 middle news in an even dataset

# In[5]:


def median(*args):
    if len(args) % 2 == 0:
        # you use round() to leave you at the number immediately right to the center
        i = round((len(args) + 1) / 2) 
        j = i - 1
        return ((args[i] + args[j]) / 2)
    
    else:
        k = round(len(args)/ 2)
        return args[k]  


# In[6]:


def sort_and_median(*args):
    sorted_list = []
    for arg in args:
        sorted_list += arg
        sorted_list.sort()
    
    if len(sorted_list) % 2 == 0:
        i = round((len(sorted_list) + 1) / 2)
        j = i - 1
        return ((sorted_list[i] + sorted_list[j]) / 2)
    
    else:
        k = round(len(sorted_list)/ 2)
        return sorted_list[k]


# In[7]:


even_list = [85, 13, 45, 67, 54, 56, 99, 75]
odd_list = [24, 56, 86, 94, 24, 33, 14, 78, 46]

# the median function works, presuming the list is PRE-SORTED
print(median(9, 10, 12, 13, 13, 13, 15, 15, 16, 16, 18, 22, 23, 24, 24, 25))

# sort_and_median takes in a list, sorts it numerically and determines the median
print(sort_and_median(even_list))
print(sort_and_median(odd_list))


# ## Mode: the number(s) that appear the most often

# In[8]:


def mode(*args):
    '''Creates a dictionary which sorts the 'number' in a list as a key
    with its corresponding value being how many times it appeared'''
    dict_vals = {i : args.count(i) for i in args}
    
    ''' Creates a list which searches for and pulls the dictionary key value (a number), 
    if its count value is the highest within the dictionary '''
    max_list = [k for k,v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list


# In[9]:


print(mode(1,2,3,3,4,5,5,4,5,5,3,3))


# ### Variance: average degree to which each point differs from the mean; measure of average dispersion of data points

# Sample Variance $\Large S^2 = \frac{\sum \limits_{i=1}^{n}(\overline{x} - x_{i})}{n-1}$  
# Population Variance $\Large \sigma^2 = \frac{\sum \limits_{i=1}^{N}(\overline{x} - \mu)}{N-1}$  

# In[10]:


def variance(*args):
    mean_value = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_value)**2
        
    denominator = len(args) - 1
    
    return numerator/denominator


# In[11]:


def variance_of_list(lista):
    mean_value = mean_for_lists(lista)
    numerator = 0
    for i in lista:
        numerator += (i - mean_value)**2
        
    denominator = len(lista) - 1
    
    return numerator/denominator


# In[12]:


test_list = [34, 46, 66, 75, 78, 85, 87, 90, 98, 99]
print(round(variance(34, 46, 66, 75, 78, 85, 87, 90, 98, 99), 2))
print(round(variance_of_list(test_list), 2))


# ### Standard Deviation:  measure of the dispersion of observations within a data set RELATIVE to their mean

# Population Standard Deviation $\Large \sigma = \sqrt{\frac{1}{N-1} \cdot \sum \limits_{i=1}^{N}(\overline{x} - \mu)^2}$ 

# In[13]:


def standard_deviation(*args):
    return math.sqrt(variance(*args))


# In[14]:


def standard_deviation_of_list(lista):
    return math.sqrt(variance_of_list(lista))


# In[15]:


print(round(standard_deviation(34, 46, 66, 75, 78, 85, 87, 90, 98, 99), 2))
print(round(standard_deviation_of_list(test_list),2))


# ### Coefficient of Variance (CV): relative dispersion of data points in a data series (multiple data sets) around the mean

# $ CV = \frac{\sigma}{\mu}$

# In[16]:


def coef_variation(*args):
    return standard_deviation(*args)/mean(*args)


# In[17]:


coef_variation(4,3,6,5,2)


# In[18]:


print(f'CV miles : {coef_variation(3,4,4.5,3.5)}')
print(f'CV KM : {coef_variation(4.828, 6.437, 7.242, 5.632)}')


# In[19]:


# the example above shows that the conversion between mi to km is identical


# ### Covariance & Correlation Coefficient (r)

# Covariance $\Large Cov = \frac{\sum \limits_{i=1}^{n}(\overline{x} - x_{i}) \cdot (\overline{y} - y_{i})}{n-1}$  

# In[20]:


market_cap = [1532, 1488, 1343, 928, 615]
earnings = [58, 35, 75, 41, 17]


# In[21]:


def covariance(list1, list2):
    # Finding the mean for each data series
    mean_list1 = mean_for_lists(list1)
    mean_list2 = mean_for_lists(list2)
    ''' Creating a list which holds the difference of the mean and 
        each individual elements for both lists
        '''
    
    sub_list1 = [i - mean_list1 for i in list1]
    sub_list2 = [i - mean_list2 for i in list2]
    
    '''
    Numerator: Multiplies the 'difference of the mean' value for both elements in the 
    same index, for the span of the list. Then, performs the summation, which sums up 
    all of the products
    ''' 
    numerator = sum([sub_list1[i]*sub_list2[i] for i in range(len(sub_list1))])
    denominator = len(list1) - 1
    cov = numerator/denominator
    return cov


# In[22]:


covariance(market_cap, earnings)


# ### The correlation coefficient (r) uses the covariance  and standard deviations to yield a more definitive measure of how 2 datasets are trending

# $\Large r = \frac{Cov(X,Y)}{S(X) \cdot S(Y)} $

# In[23]:


def correlation_coefficient(list1, list2):
    numerator = covariance(list1, list2)
    denominator = standard_deviation_of_list(list1) * standard_deviation_of_list(list2)
    return numerator/denominator


# In[24]:


print(covariance(market_cap, earnings))
print(standard_deviation_of_list(market_cap))
print(standard_deviation_of_list(earnings))
print(correlation_coefficient(market_cap, earnings))


# In[25]:


# turning the data into a dictionary then DataFrame with Pandas
import pandas as pd


# In[26]:


def hows_the_trend(r):
    if r > (-0.75) and r < 0.25:
        return 'NT'
    if r > 0.25:
        return 'pos'
    if r < -0.75:
        return 'neg'


# In[27]:


r_test = correlation_coefficient(market_cap, earnings)
print(hows_the_trend(r_test))


# In[28]:


stats = {
    'Cov' : [f'{covariance(market_cap, earnings)}'],
    'StndDevMC' : [f'{(standard_deviation_of_list(market_cap))}'],
    'StndDevE' : [f'{standard_deviation_of_list(earnings)}'],
    'r': [f'{correlation_coefficient(market_cap, earnings)}'],
    'Trend': [f'{hows_the_trend(r_test)}']
}


# In[29]:


df = pd.DataFrame.from_dict(stats)
df

