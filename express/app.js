const express = require('express')
const mysql = require('mysql2');

require("dotenv").config();

const app = express()
const port = 3000

var con = mysql.createConnection({
    host: process.env.HOST,
    user: process.env.USER,
    password: process.env.PASSWORD,
    database: "creatureDB"
});

con.connect(err => {
    if (err) console.log(err);
    console.log("Connected to database!");
});

app.get('/', (req, res) => {
  res.send('Welcome to the ARK API');
})

app.route('/creatures')

.get((req, res) => {
    con.query("SELECT * FROM creatures", (err, result, fields) => {
        if (err) console.log(err);
        res.json(result);
    })
})

app.listen(port, () => {
  console.log(`ARK API listening on port ${port}`);
})