#!/usr/bin/env python
# coding:utf-8
"""
Runs the keyword extraction algorithmn on an example
"""
__author__ = "Lavanya Sharan"


import sys
from flask import Flask, request
import os
from keywordextraction import *
import json 

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/api', methods=['GET', 'POST'])
def api():
  data = request.get_json()
  text = data["text"]
  keywords = main(text)
  return json.dumps(keywords)
    
def main(text):
  # load keyword classifier
  preload = 1
  classifier_type = 'logistic'
  keyword_classifier = get_keywordclassifier(preload,classifier_type)['model']

  # extract top k keywords
  top_k = 15
  keywords = extract_keywords(text,keyword_classifier,top_k,preload)  
  print 'ORIGINAL TEXT:\n%s\nTOP-%d KEYWORDS returned by model: %s\n' % (text,top_k,', '.join(keywords))
  return keywords

if __name__ == '__main__':
	app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
