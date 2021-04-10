# -*- encoding: utf-8 -*-
'''
@Project : Test_auto_study1
@File    :   test_calculator.py    
@Author :   maodou
@Date   : 2021/4/10 15:48
'''

import pytest
import yaml
import os


class Test_calculator:

    '''
    1.从yaml文件中获取test_add方法的测试用
    2.从yaml文件中获取test_subtraction方法的测试用例
    3.从yaml文件中获取test_multiplication方法的测试用例
    4.从yaml文件中获取test_division方法的测试用例
    '''

    with open(os.path.join(os.path.abspath("."), 'testcase_add.yaml')) as v:
        testcaseaddfile = v.read()
    testcase_add = yaml.load(testcaseaddfile)

    with open(os.path.join(os.path.abspath("."), 'testcase_sub.yaml')) as f:
        testcasesubfile = f.read()
    testcase_sub = yaml.load(testcasesubfile)

    with open(os.path.join(os.path.abspath("."), 'testcase_mul.yaml')) as r:
        testcasemulfile = r.read()
    testcase_mul = yaml.load(testcasemulfile)

    with open(os.path.join(os.path.abspath("."), 'testcase_div.yaml')) as r:
        testcasedivfile = r.read()
    testcase_div = yaml.load(testcasedivfile)

    def setup_class(self):
        print("计算开始")

    @pytest.mark.parametrize('a,b,expect', testcase_add)
    def test_add(self, a, b, expect):
        if a or b or expect == float:
            assert expect == round(a + b, 2)
        else:
            assert expect == a + b

    @pytest.mark.parametrize('a,b,expect', testcase_sub)
    def test_subtraction(self, a, b, expect):

        if a or b or expect == float:
            assert expect == round(a - b, 2)
        else:
            assert expect == a - b

    @pytest.mark.parametrize('a,b,expect', testcase_mul)
    def test_multiplication(self, a, b, expect):

        if a or b or expect == float:
            assert expect == round(a * b, 2)
        else:
            assert expect == a * b

    @pytest.mark.parametrize('a,b,expect', testcase_div)
    def test_division(self, a, b, expect):

        try:
            if a or b or expect == float:
                assert expect == round(a / b, 2)
            else:
                assert expect == a / b

        except ZeroDivisionError as e:
            print(e)

    def teardown_class(self):
        print("计算结束")


