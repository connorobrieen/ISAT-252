
const fizz = function (x) {
    // check to see if x exists
    if (typeof x !== 'undefined') {
        // yes, x exists, carry on
    } else {
        // no, x does not exist, throw an error
        throw new Error('there is no input')
    }
}


module.exports = {
    'fizz': fizz
}