#!/bin/bash
ps ax | grep multiple.py | grep -v grep | awk '{print $1}' | xargs kill -9
