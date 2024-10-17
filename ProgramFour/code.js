const checkTraingle = (a,b,c) => {
    if(a === b && b === c && c === a) return 'Equalateral Triangle'
    if(a === b || b === c || c === a) return 'Isosceles Triangle'
    return "Scalene Triangle"
}

console.log(checkTraingle(1,2,3));
console.log(checkTraingle(3,2,2));
console.log(checkTraingle(3,3,3));