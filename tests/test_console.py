#!/usr/bin/python3

import unittest
import os
from io import StringIO
import sys
from console import HBNBCommand
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ class test """

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        s = f.getvalue()[:-1]
        self.assertEqual(s, "** class name missing **")

    def test_false_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create nob")
        s = f.getvalue()[:-1]
        self.assertEqual(s, "** class doesn't exist **")

    def test_exist_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        s = f.getvalue()[:-1]
        self.assertEqual(len(s), 36)

    def test_room_nbr(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State number_rooms=2')
            HBNBCommand().onecmd('all State')
        s = f.getvalue()
        self.assertTrue("'number_rooms': 2" in s)

    def test_longitude(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State longitude=-12.43789')
            HBNBCommand().onecmd('all State')
        s = f.getvalue()
        self.assertTrue("longitude': -12.43789" in s)

    def test_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            HBNBCommand().onecmd('all State')
        s = f.getvalue()[:-1]
        self.assertTrue("California" in s)
