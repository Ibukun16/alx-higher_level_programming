#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, result, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const value = data.characters;
  for (const n of value) {
    request.get(n, function (error, result, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
