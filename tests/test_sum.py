import pytest

from pkg.sum import sum

def testMethod_sum_5_5_10():
	assert(sum(5,5) == 10)

def testMethod_sum_2_5_7():
	assert(sum(2,5) == 7)
    
def testMethod_sum_1_5_6():
	assert(sum(1,5) == 6)
       
def testMethod_sum_0_5_5():
	assert(sum(0,5) == 5)   
    
def testMethod_sum__6_5_1():
	assert(sum(-6,5) == -1)
       
def testMethod_sum_0_0_0():
	assert(sum(0,0) == 0)
    
def testMethod_sum_2__1_1():
	assert(sum(2,-1) == 1)
    
    