#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    // parse the JSON data and extract the "results" array
    const results = JSON.parse(body).results;
    // Use the 'reduce()' method to iterate through the movies in the 'results' array.
    console.log(results.reduce((count, movie) => {
      // check if there is a character with ID 18 ('/18/') in the 'characters' array.
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
