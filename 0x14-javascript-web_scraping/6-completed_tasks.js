#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const n in tasks) {
      const task = tasks[n];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
