#!/usr/bin/node
// 101-compute.js
const data = require('./101-data');
const initialDict = data.dict;

// Initialize a new dictionary
const newDict = {};

// Loop through the initial dictionary
for (const userId in initialDict) {
  const occurrences = initialDict[userId];

  // If occurrences is not a key in the new dictionary, create it
  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  // Add the user id to the list of user ids for the corresponding occurrences
  newDict[occurrences].push(userId);
}

console.log(newDict);
