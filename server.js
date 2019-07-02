const express = require("express");
const csv2json = require("csv2json");
const fs = require("fs")
const app = express();
try {
        app.listen(80,() => {console.log("Web Server Hosted on port 8$
        app.use(express.static("public"));
        app.get("/api/csv",(req,res) => {
                res.sendFile("/home/pi/public/data.txt")
        });
        app.get("/api/json",(req,res) => {
                res.setHeader('Content-Type', 'text/plain');
                res.json(csv2json(fs.readFileSync("/home/pi/public/da$
        })
} catch(err) {
        console.log("An Error Has Occurred...");
}







