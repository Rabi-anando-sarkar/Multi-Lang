const isPalindrome = (str) => {
    const revStr = str.split('').reverse().join("")
    if(str === revStr) return true
    return false
}

console.log(isPalindrome('racecar'));
console.log(isPalindrome('naman'));
console.log(isPalindrome('rabi'));
