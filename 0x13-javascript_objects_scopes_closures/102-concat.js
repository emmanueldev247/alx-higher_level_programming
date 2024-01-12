#!/usr/bin/node
const fs = require('fs');

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const outputFile = process.argv[4];

const content1 = fs.readFileSync(firstFile, 'utf-8');
const content2 = fs.readFileSync(secondFile, 'utf-8');

const joinedContent = content1 + content2;

fs.writeFileSync(outputFile, joinedContent, 'utf-8');
