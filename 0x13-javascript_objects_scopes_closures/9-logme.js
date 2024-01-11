#!/usr/bin/node
let countArg = 0;

exports.logMe = function (item) {
  console.log(`${countArg}: ${item}`);
  countArg++;
};
