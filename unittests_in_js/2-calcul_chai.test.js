const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js'); // if tests live in ./test, use ../2-calcul_chai.js

describe('calculateNumber(type, a, b) — Chai expect', function () {
  describe('SUM', function () {
    it("matches example: SUM(1.4, 4.5) -> 6", function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('rounds both then adds (various)', function () {
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);  // 1 + 4
      expect(calculateNumber('SUM', 1.5, 3.5)).to.equal(6);  // 2 + 4
      expect(calculateNumber('SUM', 0.49, 0.49)).to.equal(0); // 0 + 0
      expect(calculateNumber('SUM', 0.5, 0.5)).to.equal(2);   // 1 + 1
    });

    it('handles negatives', function () {
      expect(calculateNumber('SUM', -1.2, -3.7)).to.equal(-5); // -1 + -4
      expect(calculateNumber('SUM', -1.5, 3.2)).to.equal(2);   // -1 + 3
    });
  });

  describe('SUBTRACT', function () {
    it("matches example: SUBTRACT(1.4, 4.5) -> -4", function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('rounds both then subtracts (a - b)', function () {
      expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2); // 2 - 4
      expect(calculateNumber('SUBTRACT', 0.49, 0.49)).to.equal(0); // 0 - 0
      expect(calculateNumber('SUBTRACT', 0.5, 0.49)).to.equal(1);  // 1 - 0
      expect(calculateNumber('SUBTRACT', 0.49, 0.5)).to.equal(-1); // 0 - 1
    });

    it('handles negatives', function () {
      // Math.round(-1.5) = -1, Math.round(-3.5) = -3 => -1 - (-3) = 2
      expect(calculateNumber('SUBTRACT', -1.5, -3.5)).to.equal(2);
      expect(calculateNumber('SUBTRACT', -1.2, 3.2)).to.equal(-4); // -1 - 3
    });
  });

  describe('DIVIDE', function () {
    it("matches example: DIVIDE(1.4, 4.5) -> 0.2", function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2); // 1 / 5
    });

    it("matches example: DIVIDE(1.4, 0) -> 'Error'", function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error'); // 1 / 0 (rounded)
    });

    it('rounds both then divides (various)', function () {
      expect(calculateNumber('DIVIDE', 5.5, 2)).to.equal(3);       // 6 / 2
      expect(calculateNumber('DIVIDE', 3.1, 2.5)).to.equal(1);     // 3 / 3
      expect(calculateNumber('DIVIDE', 0.4, 4.6)).to.equal(0);     // 0 / 5
      expect(calculateNumber('DIVIDE', -2.5, 3.5)).to.equal(-0.5); // -2 / 4
      expect(calculateNumber('DIVIDE', -1.5, -3.5)).to.equal(1/3); // -1 / -3
    });

    it("returns 'Error' when rounded denominator is 0 (including negative zero)", function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');   // 1 / 0
      expect(calculateNumber('DIVIDE', 1.4, -0.4)).to.equal('Error');  // 1 / -0 (treated as 0)
      expect(calculateNumber('DIVIDE', 1.4, -0.5)).to.equal('Error');  // rounds to -0
    });

    it('does NOT return Error when rounded denominator is ±1', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.5)).to.equal(1);   // 1 / 1
      expect(calculateNumber('DIVIDE', 1.4, -0.6)).to.equal(-1); // 1 / -1
    });
  });

  describe('Invalid type', function () {
    it('throws TypeError for unexpected type', function () {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw(TypeError);
    });
  });
});
