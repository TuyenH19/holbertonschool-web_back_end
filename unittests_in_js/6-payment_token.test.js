// 6-payment_token.test.js
const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
  it('resolves with the expected data when success === true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        try {
          assert.deepStrictEqual(res, { data: 'Successful response from the API' });
          done();
        } catch (err) {
          done(err); // fail the test if assertion throws
        }
      })
      .catch(done); // fail the test if the promise rejects
  });
});
