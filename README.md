# TECHA: Technical Analysis Library

Collection of Technical Analysis Functions

 * __Author__: Daniel J. Umpierrez
 * __Version__: 0.1.1
 * __License__: MIT

## Description

This project try to merge some Technical Analysis open source projects
like finta, ta-lib, ... into one.

## Requirements
 + Pandas: https://github.com/pandas-dev/pandas
 + FinTA: http://github.com/havocesp/finta
 + TA-Lib: https://github.com/mrjbq7/ta-lib

# Changelog

## Version 0.1.1

 * New TaLib class method structure for easy access to all functions
 * Dome function documentation writed (take a look at "doc" directory)
 *

## Version 0.1.0

 * Minor fixes
 * Some code restructuration
 * New import style at core module

## Version 0.0.9

 * Added method _get_info_ who will dispatch indicator info request
   if available.
 * Added class atribute _lib_ for let users to set **finta** as primary
   libary instead the default one (**ta-lib**).
 * Added a method to obtain _finta_ lib supported indictators as list.

# TODO list

 * [ ] Make the project suitable for a _pip_ install.
 * [x] Start with documentation tasks.
 * [x] Find a way to easyly access to all funtions from a uniq point.

## How to contribute

Any kind of help is welcome, send code by using pull functions, write
documentation, or give ideas...

