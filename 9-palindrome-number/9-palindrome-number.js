/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let str = String(x);
    let opp = str.split("").reverse().join("");
    return str === opp
};