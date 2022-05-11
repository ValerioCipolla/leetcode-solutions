/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    for (let i = strs[0].length; i > 0; i--) {
        let sliced = strs[0].slice(0, i)
        let matches = true;
        for (let j = 0; j < strs.length; j++) {
            if (!strs[j].startsWith(sliced)) {
                matches = false;
            } 
        }
        if (matches) {
            return sliced
        }
    }
    return ""
};