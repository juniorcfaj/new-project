#!/usr/bin/env bash

locust -f locustfile.py --host https://newudacityapp.azurewebsites.net/ --users 500 --spawn-rate 5 
