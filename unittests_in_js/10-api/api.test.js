const { expect } = require('chai');
const { application } = require('express');
const request = require('request');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865/';
  it('Correct status code?', (done) => {
    request.get(baseUrl, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(baseUrl, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Content-Type header?', (done) => {
    request.get(baseUrl, (err, res) => {
      expect(err).to.be.null;
      expect(res.headers['content-type']).to.include('text/html');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865/cart';

  it('Correct status code when :id is a number', (done) => {
    request.get(`${baseUrl}/12`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct body when :id is a number', (done) => {
    request.get(`${baseUrl}/12`, (err, _res, body) => {
      expect(err).to.be.null;
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('404 when :id is NOT a number', (done) => {
    request.get(`${baseUrl}/hello`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('404 when :id is a negative number (not matched by \\d+)', (done) => {
    request.get(`${baseUrl}/-3`, (err, res) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe('GET /available_payments', () => {
  const url = 'http://localhost:7865/available_payments';
  const expected = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };

  it('returns status 200 and JSON content-type', (done) => {
    request.get(url, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res.statusCode).to.equal(200);
      expect(res.headers['content-type']).to.include('application/json');
      done();
    });
  });

  it('returns the expected object (deep equal)', (done) => {
    request.get(url, (err, _res, body) => {
      expect(err).to.be.null;
      const parsed = JSON.parse(body);
      expect(parsed).to.deep.equal(expected);
      done();
    });
  });
});

describe('POST /login', () => {
  const url = 'http://localhost:7865/login';

  it('returns status 200 and correct welcome message', (done) => {
    request.post(
      {
        url,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userName: 'Betty' })
      },
      (err, res, body) => {
        expect(err).to.be.null;
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      }
    );
  });
});
