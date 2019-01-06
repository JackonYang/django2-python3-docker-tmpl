#!/bin/bash

dir=`pwd`

name=`basename $dir`

p1=`dirname $dir`
p1_basename=`basename $p1`

echo $p1_basename'_'$name | awk '{print tolower($0)}'