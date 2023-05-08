#!/usr/bin/node
//Star Wars API
const request = require('request');
const urlMovie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
//make a request to the Star Wars API


request(urlMovie, async function (error, response, body) {
  const arr = [];
//calling the arg urlmovie
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    for (let i = 0; i < film.characters.length; i++) {
      arr.push(myCharacter(film.characters[i]));
    }
  }

  let actors = await Promise.all(arr);

  actors = actors.map((actor) => JSON.parse(actor).name);
  actors.forEach((actor) => console.log(actor));
});
///mapping over the results
function myCharacter (thisCharacter) {
  return new Promise((resolve, reject) => {
    request(thisCharacter, function (error, response, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}

