// 8-api/api.test.js
const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(baseUrl, (err, res, _body) => {
      expect(err).to.be.null;
      expect(res && res.statusCode).to.equal(200);
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

  it('Other? (Content-Type header)', (done) => {
    request.get(baseUrl, (err, res, _body) => {
      expect(err).to.be.null;
      // Express sends strings as text/html by default
      expect(res.headers['content-type']).to.include('text/html');
      done();
    });
  });
});
