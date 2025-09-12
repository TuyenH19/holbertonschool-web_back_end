// 8-api/api.js
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// Numeric-only cart id using a regex in the path
// NOTE: because this is a JS string, we escape the backslash -> '\\d+'
app.get('/cart/:id(\\d+)', (req, res) => {
  const { id } = req.params;
  res.send(`Payment methods for cart ${id}`);
});

const PORT = 7865;
app.listen(PORT, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;
