import express from "express";

const app = express();

app.get("/", (req, res) => res.send( {info: 'Home'}));

app.listen(8001);