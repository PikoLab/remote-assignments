const array1 = [1,2,4,5];
const array2 = [5,2,7,1,6];
const array3 = [5,2,7,7,7,1,6];


function max(numbers){
    let max_num=0;
    for (let i = 0; i < numbers.length; i+=1){
        if (numbers[i] > max_num) {
            max_num = numbers[i];
        }
    }
    return max_num 
}


function findPosition(numbers,target){
    let position = -1
    for (let i = 0; i < numbers.length; i+=1){
        if (numbers[i] === target) {
            position = i
            return position
        }
    }
    return position
}

console.log(`Find max number in [${array1}]: The answer is ${max(array1)}.`);
console.log(`Find max number in [${array2}]: The answer is ${max(array2)}.`);
console.log(`Find position of target ${5} in arry [${array2}]: The answer is ${findPosition(array2,5)}.` ); // should print 0
console.log( `Find position of target ${7} in arry [${array2}]: The answer is ${findPosition(array2,7)}.`); // should print 2
console.log( `Find position of target ${7} in arry [${array3}]: The answer is ${findPosition(array3,7)}.`); // should print 2 (the first one)
console.log( `Find position of target ${8} in arry [${array2}]: The answer is ${findPosition(array2,8)}.`); // should print -1