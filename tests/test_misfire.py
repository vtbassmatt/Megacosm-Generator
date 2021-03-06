#!/usr/bin/env python
# -*- coding: utf-8 -*-

from megacosm.generators import Misfire
import unittest2 as unittest

import redis
from config import TestConfiguration


class TestMisfire(unittest.TestCase):

    def setUp(self):
        """  """
        self.redis = redis.from_url(TestConfiguration.REDIS_URL)

    def test_random_misfire(self):
        """  """
        misfire = Misfire(self.redis)
        print misfire.text
        self.assertNotEqual(misfire.text, '')
        self.assertEqual('%s' % misfire, misfire.text)
