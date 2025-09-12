// 3-payment.test.js
const assert = require('assert');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  afterEach(function () {
    sinon.restore(); // clean up all spies after each test
  });

  it('should call Utils.calculateNumber with SUM, 100, 20', function () {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(calcSpy.calledOnce, true);
    assert.strictEqual(
      calcSpy.calledWithExactly('SUM', 100, 20),
      true,
      'Utils.calculateNumber not called with expected arguments'
    );
  });

  it('should log the correct total to the console', function () {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Verify the math was done using Utils
    assert.strictEqual(calcSpy.calledOnceWithExactly('SUM', 100, 20), true);

    // The result of SUM(100, 20) after rounding is 120
    assert.strictEqual(logSpy.calledOnceWithExactly('The total is: 120'), true);
  });
});
