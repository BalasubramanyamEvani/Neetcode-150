/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    for (const key in Object.keys(obj)) {
        return false;
    }
    return true;
};