#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    findcharacter(characters, 0);
  }
});

function findcharacter (characters, idx) {
  request(characters[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        findcharacter(characters, ++idx);
      }
    }
  });
}
