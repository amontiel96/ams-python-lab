# -*- coding: utf-8 -*-
from unittest import TestCase
from src.lambdas.ams_lambda.lambda_function import lambda_handler


class Test(TestCase):

    def setUp(self) -> None:
        self.eventLogs = {}

    def test_lambda_handler_logs(self):
        print(
            "-------------------------------start test_lambda_handler_logs-------------------------------------------")
        result = lambda_handler(self.eventLogs, None)
        print(result)

