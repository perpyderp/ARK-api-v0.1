/*
    Author: Jacob Cuison
    Entry point for the ARK API, and sets up the middleware, routes, and error handling

*/

const express = require('express')
const mysql = require('mysql2');
const creatureRoutes = require('../routes/creatureRoutes');
const armorRoutes = require('../routes/armorRoutes');

require('dotenv').config({ path: '../../.env' });

const app = express()
const port = 3000;
app.use(express.json());
app.use('/api', [creatureRoutes, armorRoutes]);

app.listen(port, () => {
  console.log(`ARK API listening on port ${port}`);
})