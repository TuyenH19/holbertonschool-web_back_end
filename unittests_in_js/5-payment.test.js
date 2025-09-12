const assert = require('assert');
const sinon = require('sinon');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi (hooks + one spy)', function () {
  let logSpy;

  beforeEach(function () {
    // One spy: only on console.log
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    // Always restore to avoid cross-test leakage
    logSpy.restore();
  });

  it('logs the correct message and only once for (100, 20)', function () {
    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(logSpy.calledOnce, true, 'console.log should be called once');
    assert.strictEqual(
      logSpy.calledWithExactly('The total is: 120'),
      true,
      'console.log should be called with "The total is: 120"'
    );
  });

  it('logs the correct message and only once for (10, 10)', function () {
    sendPaymentRequestToApi(10, 10);

    assert.strictEqual(logSpy.calledOnce, true, 'console.log should be called once');
    assert.strictEqual(
      logSpy.calledWithExactly('The total is: 20'),
      true,
      'console.log should be called with "The total is: 20"'
    );
  });
});
