#!/usr/bin/node
const request = require('request');
const themovieId = process.argv[2];
const theoptions = {
  url: 'https://swapi-api.hbtn.io/api/films/' + themovieId,
  method: 'GET'
};

request(theoptions, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
