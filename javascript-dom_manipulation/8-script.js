#!/usr/bin/node
document.addEventListener("DOMContentLoaded", function () {
    fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(response => response.json)
    .then(data =>{
        document.querySelector("#hello").textcontent = data.hello;
    });
});