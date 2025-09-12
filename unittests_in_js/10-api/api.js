// 8-api/api.js
const express = require('express');

const app = express();

// Using Express middleware to parse JSON and urlencoded data
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Numeric-only cart id using a regex in the path
// NOTE: because this is a JS string, we escape the backslash -> '\\d+'
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const userName = req.body && req.body.userName;
  res.status(200).send(`Welcome ${userName}`);
});

const PORT = 7865;
app.listen(PORT, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
