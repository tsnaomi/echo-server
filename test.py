#!/usr/bin/env python

import unittest
import socket
import echo_client

class TestEchoChamber(unittest.TestCase):

    def test_short(self):
        short_message = "darling"
        self.assertEqual(short_message, echo_client.echo_client(short_message))

    def test_long(self):
        long_message = "3.1415926535897932384626433832795028841971693993"
        self.assertEqual(long_message, echo_client.echo_client(long_message))

    def test_exact(self):
        exact_message = "abcdefghijklmnopqrstuvwxyz123456"
        self.assertEqual(exact_message, echo_client.echo_client(exact_message))

if __name__ == '__main__':
    unittest.main()
