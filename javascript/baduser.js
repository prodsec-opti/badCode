const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');

// Vulnerable endpoint
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;
// sample changes
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'testdb',
    });

    connection.query(query, (err, results) => {
       //to do ...
    });

});