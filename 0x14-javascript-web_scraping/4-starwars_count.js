#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((n, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? ++n
        : n;
    }, 0));
  }
});
