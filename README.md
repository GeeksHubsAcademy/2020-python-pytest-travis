# 2020-python-pytest-travis

<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>

[![Build Status](https://travis-ci.com/geekshubs/2020-python-pytest-travis.svg?branch=master)](https://travis-ci.com/geekshubs/2020-python-pytest-travis)
```
$ cd vicboma1/2020-python-pytest-travis

$ git checkout -qf efa9a19a9b9f0c68943805e2c93dee3ac4b38abf
0.01s0.01s$ source ~/virtualenv/python3.6/bin/activate

$ python --version
Python 3.6.3

$ pip --version
pip 9.0.1 from /home/travis/virtualenv/python3.6.3/lib/python3.6/site-packages (python 3.6)
install
1.03s

$ pip install -e .
Obtaining file:///home/travis/build/vicboma1/2020-python-pytest-travis
Installing collected packages: Testing-with-PytTest
  Running setup.py develop for Testing-with-PytTest
Successfully installed Testing-with-PytTest
0.34s

$ pytest
============================= test session starts ==============================

platform linux -- Python 3.6.3, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: /home/travis/build/vicboma1/2020-python-pytest-travis, inifile:
collected 9 items                                                              
tests/test_fib.py ..                                                     [ 22%]
tests/test_sum.py .......                                                [100%]

=========================== 9 passed in 0.03 seconds ===========================

The command "pytest" exited with 0.
```
