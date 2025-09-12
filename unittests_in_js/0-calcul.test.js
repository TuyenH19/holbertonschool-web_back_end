const assert = require('assert');
const calculateNumber = require('./0-calcul.js'); // if this file lives in ./test, change to ../0-calcul.js

describe('calculateNumber', function () {
  // --- Your explicit examples (4 tests) ---
  it('adds (1, 3) -> 4', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('rounds b (1, 3.7) -> 5', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds both (1.2, 3.7) -> 5', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('handles .5 rule (1.5, 3.7) -> 6', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  // --- Systematic rounding grid (126 tests) ---
  // 9 a-values × 14 b-values = 126
  const aValues = [-2.5, -1.7, -1.5, -1.2, -0.5, -0.1, 0, 0.49, 0.5];
  const bValues = [-3.5, -2.6, -2.5, -1.51, -1.5, -1.1, -0.5, -0.1, 0, 0.49, 0.5, 1.2, 1.5, 1.7];

  aValues.forEach((a) => {
    bValues.forEach((b) => {
      it(`rounds a=${a} and b=${b}`, function () {
        const expected = Math.round(a) + Math.round(b);
        assert.strictEqual(calculateNumber(a, b), expected);
      });
    });
  });
});
