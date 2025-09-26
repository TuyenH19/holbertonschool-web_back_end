import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

/* -----------------------------
   Data
------------------------------ */
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

/* -----------------------------
   Redis (promisified)
------------------------------ */
const client = redis.createClient();
client.on('error', (err) => console.error('Redis error:', err));

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
  // store "reserved" count under key item.<ID>
  await setAsync(`item.${itemId}`, String(stock));
}

async function getCurrentReservedStockById(itemId) {
  const val = await getAsync(`item.${itemId}`);
  return Number(val) || 0;
}

/* -----------------------------
   Express server
------------------------------ */
const app = express();
const PORT = 1245;

// List all products
app.get('/list_products', (_req, res) => {
  const payload = listProducts.map((p) => ({
    itemId: p.id,
    itemName: p.name,
    price: p.price,
    initialAvailableQuantity: p.stock,
  }));
  res.json(payload);
});

// Product detail with current available quantity
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reserved = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - reserved;

  return res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Reserve one product (if available)
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const reserved = await getCurrentReservedStockById(itemId);
  const available = product.stock - reserved;

  if (available <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: product.id });
  }

  await reserveStockById(itemId, reserved + 1);
  return res.json({ status: 'Reservation confirmed', itemId: product.id });
});

app.listen(PORT, () => {
  // eslint-disable-next-line no-console
  console.log(`API available on localhost port ${PORT}`);
});
