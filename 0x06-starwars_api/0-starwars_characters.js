#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.log('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];
const apiURL = `https://swapi.dev/api/films/${movieId}/`;

request(apiURL, (error, response, body) => {
    if (error) {
        console.error(error);
        process.exit(1);
    }
    if (response.statusCode !== 200) {
        console.error(`Error ${response.statusCode} - ${response.statusMessage}`);
        process.exit(1);
    }

    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach((charactersUrl) => {
        request(charactersUrl, (error, res, messBody) => {
            if (error) {
                console.error(error);
            } else {
                const character = JSON.parse(messBody);
                console.log(character.name);
            }
        });
    });
});