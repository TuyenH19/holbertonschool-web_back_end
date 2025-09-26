import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const KEY = 'HolbertonSchools';
const cities = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// Helper: set fields sequentially so we can use callbacks (and log with redis.print)
function setHashFieldsSequentially(key, fieldsObj, done) {
  const entries = Object.entries(fieldsObj);

  const next = (i) => {
    if (i >= entries.length) return done();

    const [field, value] = entries[i];
    client.hset(key, field, value, (err, reply) => {
      // Must use redis.print for each hset
      redis.print(err, reply);
      next(i + 1);
    });
  };

  next(0);
}

// Execute: create hash, then display hash
setHashFieldsSequentially(KEY, cities, () => {
  client.hgetall(KEY, (err, obj) => {
    if (err) {
      console.error(err);
    } else {
      console.log(obj);
      // Expected shape:
      // {
      //   Portland: '50',
      //   Seattle: '80',
      //   'New York': '20',
      //   Bogota: '20',
      //   Cali: '40',
      //   Paris: '2'
      // }
    }
    client.quit();
  });
});
