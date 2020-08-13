#!/usr/bin/python3

import unittest
import os
from io import StringIO
import sys
from console import HBNBCommand
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ class test """

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        s = f.getvalue()[:-1]
        self.assertEqual(s, "* class name missing *")

    def test_false_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create nob")
        s = f.getvalue()[:-1]
        self.assertEqual(s, "* class doesn't exist *")

    def test_exist_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        s = f.getvalue()[:-1]
        self.assertEqual(len(s), 36)
