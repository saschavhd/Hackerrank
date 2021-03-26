
function reverseString(s) {
    try {
        // let y = ''.join(s.split('').reverse())
        console.log(s.split('').reverse().join(''));
    }
    catch(err) {
        console.log("s.split is not a function");
        console.log(s);
    }
}
