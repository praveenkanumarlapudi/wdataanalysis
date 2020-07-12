{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 AndaleMono;}
{\colortbl;\red255\green255\blue255;\red38\green38\blue38;\red41\green142\blue11;\red26\green125\blue169;
\red148\green108\blue71;\red255\green255\blue255;\red77\green80\blue81;\red187\green24\blue34;}
{\*\expandedcolortbl;;\cssrgb\c20000\c20000\c20000;\cssrgb\c18431\c61176\c3922;\cssrgb\c9804\c56471\c72157;
\cssrgb\c65098\c49804\c34902;\cssrgb\c100000\c100000\c100000\c49804;\cssrgb\c37255\c38824\c39216;\cssrgb\c78824\c17255\c17255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl320\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from __future__ \cf3 \strokec3 import\cf2 \strokec2  print_function\
from pyspark \cf3 \strokec3 import\cf2 \strokec2  SparkContext\
\pard\pardeftab720\sl320\partightenfactor0
\cf3 \strokec3 import\cf2 \strokec2  sys\
\pard\pardeftab720\sl320\partightenfactor0
\cf4 \strokec4 if\cf2 \strokec2  __name__ \cf5 \cb6 \strokec5 ==\cf2 \cb1 \strokec2  \cf3 \strokec3 "__main__"\cf7 \strokec7 :\cf2 \strokec2 \
    \cf4 \strokec4 if\cf2 \strokec2  len\cf7 \strokec7 (\cf2 \strokec2 sys\cf7 \strokec7 .\cf2 \strokec2 argv\cf7 \strokec7 )\cf2 \strokec2  \cf5 \cb6 \strokec5 !=\cf2 \cb1 \strokec2  \cf8 \strokec8 3\cf7 \strokec7 :\cf2 \strokec2 \
        print\cf7 \strokec7 (\cf3 \strokec3 "Usage: wordcount  "\cf7 \strokec7 ,\cf2 \strokec2  \cf3 \strokec3 file\cf5 \cb6 \strokec5 =\cf2 \cb1 \strokec2 sys\cf7 \strokec7 .\cf2 \strokec2 stderr\cf7 \strokec7 )\cf2 \strokec2 \
        \cf4 \strokec4 exit\cf7 \strokec7 (\cf8 \strokec8 -1\cf7 \strokec7 )\cf2 \strokec2 \
    sc \cf5 \cb6 \strokec5 =\cf2 \cb1 \strokec2  SparkContext\cf7 \strokec7 (\cf2 \strokec2 appName\cf5 \cb6 \strokec5 =\cf3 \cb1 \strokec3 "WordCount"\cf7 \strokec7 )\cf2 \strokec2 \
    text_file \cf5 \cb6 \strokec5 =\cf2 \cb1 \strokec2  sc\cf7 \strokec7 .\cf2 \strokec2 textFile\cf7 \strokec7 (\cf2 \strokec2 sys\cf7 \strokec7 .\cf2 \strokec2 argv\cf7 \strokec7 [\cf8 \strokec8 1\cf7 \strokec7 ])\cf2 \strokec2 \
    counts \cf5 \cb6 \strokec5 =\cf2 \cb1 \strokec2  text_file\cf7 \strokec7 .\cf2 \strokec2 flatMap\cf7 \strokec7 (\cf2 \strokec2 lambda line\cf7 \strokec7 :\cf2 \strokec2  line\cf7 \strokec7 .\cf3 \strokec3 split\cf7 \strokec7 (\cf3 \strokec3 " "\cf7 \strokec7 )).\cf2 \strokec2 map\cf7 \strokec7 (\cf2 \strokec2 lambda word\cf7 \strokec7 :\cf2 \strokec2  \cf7 \strokec7 (\cf2 \strokec2 word\cf7 \strokec7 ,\cf2 \strokec2  \cf8 \strokec8 1\cf7 \strokec7 )).\cf2 \strokec2 reduceByKey\cf7 \strokec7 (\cf2 \strokec2 lambda a\cf7 \strokec7 ,\cf2 \strokec2  b\cf7 \strokec7 :\cf2 \strokec2  a \cf5 \cb6 \strokec5 +\cf2 \cb1 \strokec2  b\cf7 \strokec7 )\cf2 \strokec2 \
    counts\cf7 \strokec7 .\cf2 \strokec2 saveAsTextFile\cf7 \strokec7 (\cf2 \strokec2 sys\cf7 \strokec7 .\cf2 \strokec2 argv\cf7 \strokec7 [\cf8 \strokec8 2\cf7 \strokec7 ])\cf2 \strokec2 \
    sc\cf7 \strokec7 .\cf2 \strokec2 stop\cf7 \strokec7 ()\
\
\
}