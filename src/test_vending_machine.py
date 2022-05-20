"""
Vending Machine Kata using doc as test.
"""
import os
import pytest
from doc_as_test_pytest import DocAsTest, doc, doc_module



def test_introduction(doc):
    """
    In this exercise you will build the brains of a vending machine. 
    It will accept money, make change, maintain inventory, and dispense products. 
    All the things that you might expect a vending machine to accomplish. 
    Features are detailed below.
    """

    doc.write("You can write in your test the information you want to see in your documentation.")

