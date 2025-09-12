const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber(type, a, b)', function () {
  describe('SUM', function () {
    it("matches example: SUM(1.4, 4.5) -> 6", function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('rounds both then adds', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5); // 1 + 4
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.5), 6); // 2 + 4
      assert.strictEqual(calculateNumber('SUM', 0.49, 0.49), 0); // 0 + 0
      assert.strictEqual(calculateNumber('SUM', 0.5, 0.5), 2); // 1 + 1
    });

    it('handles negatives', function () {
      assert.strictEqual(calculateNumber('SUM', -1.2, -3.7), -5); // -1 + -4
      assert.strictEqual(calculateNumber('SUM', -1.5, 3.2), 2);  // -1 + 3
    });
  });

  describe('SUBTRACT', function () {
    it("matches example: SUBTRACT(1.4, 4.5) -> -4", function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('rounds both then subtracts (a - b)', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 3.7), -2); // 2 - 4
      assert.strictEqual(calculateNumber('SUBTRACT', 0.49, 0.49), 0); // 0 - 0
      assert.strictEqual(calculateNumber('SUBTRACT', 0.5, 0.49), 1);  // 1 - 0
      assert.strictEqual(calculateNumber('SUBTRACT', 0.49, 0.5), -1); // 0 - 1
    });

    it('handles negatives', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.5, -3.5), 3); // -1 - (-4)
      assert.strictEqual(calculateNumber('SUBTRACT', -1.2, 3.2), -4); // -1 - 3
    });
  });

  describe('DIVIDE', function () {
    it("matches example: DIVIDE(1.4, 4.5) -> 0.2", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2); // 1 / 5
    });

    it("matches example: DIVIDE(1.4, 0) -> 'Error'", function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error'); // 1 / 0 (rounded)
    });

    it('rounds both then divides', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 5.5, 2), 3);   // 6 / 2
      assert.strictEqual(calculateNumber('DIVIDE', 3.1, 2.5), 1.5); // 3 / 2
      assert.strictEqual(calculateNumber('DIVIDE', 0.4, 4.6), 0);   // 0 / 5
      assert.strictEqual(calculateNumber('DIVIDE', -2.5, 3.5), -0.5); // -2 / 4
    });

    it('returns Error when rounded denominator is 0 (including negative zero)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');   // 1 / 0
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.4), 'Error');  // 1 / -0 (treated as 0)
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.5), 'Error');  // rounds to -0 -> Error
    });

    it('does NOT return Error when rounded denominator is ±1', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.5), 1);  // 1 / 1
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, -0.6), -1); // 1 / -1
    });
  });

  describe('Invalid type (optional defensive check)', function () {
    it('throws for unexpected type', function () {
      assert.throws(() => calculateNumber('MULTIPLY', 1, 2), /Invalid type/);
    });
  });
});
