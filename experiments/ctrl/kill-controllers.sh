#!/bin/bash
ps ax | grep floodlight | grep -v grep | awk '{print $1}' | xargs kill
