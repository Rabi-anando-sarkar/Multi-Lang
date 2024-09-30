function factorial(n) {
    let result = 1

    if(n === 0 || n === 1) {
        return result
    }

    for(let i = n; i >=  2; i--){
        result = result * i
    }

    return result
}

console.log(factorial(0));
console.log(factorial(1));
console.log(factorial(4));
console.log(factorial(5));
