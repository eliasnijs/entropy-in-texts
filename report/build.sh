#!/bin/sh

groff -ms -s -e -t -p -U -R report.troff -T ps > report.ps
ps2pdf report.ps > report.pdf
