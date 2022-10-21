#!/bin/sh

name=$(echo $1 | sed s/\.[^.]*$//g)
7z a $name.7z $1 -mx=9

