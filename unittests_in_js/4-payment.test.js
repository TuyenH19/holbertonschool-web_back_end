// 4-payment.test.js
const assert = require('assert');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi (with stub)', function () {
  afterEach(function () {
    // Ensures stubs/spies don’t leak between tests
    sinon.restore();
  });

  it("stubs Utils.calculateNumber to return 10 and checks call & console", function () {
    // Stub the expensive call
    const calcStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console to verify the message
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // 1) Stub was used with the exact arguments
    assert.strictEqual(calcStub.calledOnce, true);
    assert.strictEqual(calcStub.calledWithExactly('SUM', 100, 20), true);

    // 2) Console logged the stubbed result
    assert.strictEqual(logSpy.calledOnceWithExactly('The total is: 10'), true);
  });
});
