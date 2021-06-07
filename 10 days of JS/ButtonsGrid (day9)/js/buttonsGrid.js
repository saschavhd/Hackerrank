// Set activate button (btn5)
const act = document.getElementById('btn5');
act.addEventListener('click', rotate);

// Initialise other buttons (btn1-4,6-9)
let b1 = document.getElementById('btn1');
let b2 = document.getElementById('btn2');
let b3 = document.getElementById('btn3');
let b4 = document.getElementById('btn4');
let b6 = document.getElementById('btn6');
let b7 = document.getElementById('btn7');
let b8 = document.getElementById('btn8');
let b9 = document.getElementById('btn9');

// Array of initial positions
let arr = [1, 2, 3, 6, 9, 8, 7, 4];

function rotate() {
    // Rotate Array
    let temp = arr[arr.length-1];
    for (let i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i-1];
    }
    arr[0] = temp;

    // Set values
    b1.innerHTML = arr[0];
    b2.innerHTML = arr[1];
    b3.innerHTML = arr[2];
    b6.innerHTML = arr[3];
    b9.innerHTML = arr[4];
    b8.innerHTML = arr[5];
    b7.innerHTML = arr[6];
    b4.innerHTML = arr[7];
    return -1;
}
