const findMax = (arr) => {
    let maxNum = Math.max(...arr)
    return maxNum
}

console.log(findMax([1,5,3,9,2]));
console.log(findMax([-10,-5,-3,-9,-2]));
console.log(findMax([5]));
