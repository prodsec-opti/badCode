
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mysql = require('mysql');

// Vulnerable endpoint
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    // Vulnerable query 
//     const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

//     const connection = mysql.createConnection({
//         host: 'localhost',
//         user: 'root',
//         password: '',
//         database: 'testdb',
//     });

//     connection.query(query, (err, results) => {
//        //to do ...
//     });

// });






// Parameterized Query
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'securedb',
});

// Secure SQL query using parameterized queries
app.post('/user', (req, res) => {
    const { username, email } = req.body;

    const query = 'INSERT INTO users (username, email) VALUES (?, ?)';
    connection.query(query, [username, email], (err, result) => {
        if (err) {
            console.error('Database error:', err);
            return res.status(500).send('Internal Server Error');
        }
        res.send('User added successfully!');
    });
});
