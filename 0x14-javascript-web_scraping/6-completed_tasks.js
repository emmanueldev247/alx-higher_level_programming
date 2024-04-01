#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) { return; }

  const result = {};

  for (const todo of JSON.parse(body)) {
    if (todo.completed) {
      if (todo.userId in result) {
        result[todo.userId]++;
      } else {
        result[todo.userId] = 1;
      }
    }
  }

  console.log(result);
});
