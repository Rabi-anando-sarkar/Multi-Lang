const sortArray = (arr) => {
    const sorted = arr.sort((a,b) => a-b)
    return sorted
}

console.log(sortArray([7,10,8,11,3,4]));
