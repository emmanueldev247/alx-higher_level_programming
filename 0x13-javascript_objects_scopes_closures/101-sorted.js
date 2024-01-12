#!/usr/bin/node

const dict = require('./101-data.js').dict;

function invertDictionary (originalDict) {
  const invertedDict = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    if (!invertedDict[occurrences]) {
      invertedDict[occurrences] = [];
    }

    invertedDict[occurrences].push(userId);
  }

  return invertedDict;
}

const invertedDict = invertDictionary(dict);

console.log(invertedDict);
