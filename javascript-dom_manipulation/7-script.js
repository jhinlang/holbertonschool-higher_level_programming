#!/usr/bin/node
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    dataTransfer.results.forEach(movie =>{
        const li = document.createElement("li");
        li.textContent = movie.title;
        document.querySelector("#list_movies").appendChild(li);
    });
