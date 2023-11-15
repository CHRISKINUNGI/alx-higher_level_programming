#!/usr/bin/node
// 102-concat.js
const fs = require('fs');

// Get file paths from command line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read the contents of fileA and fileB
const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents
const concatenatedContent = contentA + '\n' + contentB;

// Write the result to fileC
fs.writeFileSync(fileC, concatenatedContent);
