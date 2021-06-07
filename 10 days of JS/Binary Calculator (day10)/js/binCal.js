// Result container
let resT = document.getElementById("res");

// Initialisation

const dflt = resT.innerHTML;
let operation = "";
let firstNum = "";
let secondNum =  "";

// Buttons
const zeroButton = document.getElementById("btn0");
const oneButton = document.getElementById("btn1");

const clearButton = document.getElementById("btnClr");
const equalButton = document.getElementById("btnEql");

const sumButton = document.getElementById("btnSum");
const subtractButton = document.getElementById("btnSub");
const multiplyButton = document.getElementById("btnMul");
const divideButton = document.getElementById("btnDiv");

// Button decleration
zeroButton.addEventListener('click', addZero);
oneButton.addEventListener('click', addOne);

clearButton.addEventListener('click', clear);
equalButton.addEventListener('click', getResult);

sumButton.addEventListener('click', addSum);
subtractButton.addEventListener('click', addSubtraction);
multiplyButton.addEventListener('click', addMultiplication);
divideButton.addEventListener('click', addDivision);

// Functions

function addZero() {
    resT.innerHTML += 0;
    if (!operation) {
        firstNum += "0";
    }
    else {
        secondNum += "0";
    }
}

function addOne() {
    resT.innerHTML += 1;
    if (!operation) {
        firstNum += "1";
    }
    else {
        secondNum += "1";
    }
}

function clear() {
    resT.innerHTML = dflt;
    operation = "";
    firstNum = 0;
    secondNum = 0;
}

function getResult() {
    if (operation == "add") {
        resT.innerHTML = (parseInt(firstNum, 2) + parseInt(secondNum, 2)).toString(2);
    }
    else if (operation == "subtract") {
        resT.innerHTML = (parseInt(firstNum, 2) - parseInt(secondNum, 2)).toString(2);
    }
    else if (operation == "multiply") {
        resT.innerHTML = (parseInt(firstNum, 2) * parseInt(secondNum, 2)).toString(2);
    }
    else if (operation == "divide") {
        resT.innerHTML = (parseInt(firstNum, 2) / parseInt(secondNum, 2)).toString(2);
    }
    firstNum = resT.innerHTML;
    secondNum = "";
    operation = "";
}

// Outdated should be simplified a lot >>>>>>>>>>

function addSum() {
    if (!operation) {
        resT.innerHTML += '+';
        operation = "add";
    }
    else {
        console.error("Error: Operator already selected.");
    }
}

function addSubtraction() {
    if (!operation) {
        resT.innerHTML += '-';
        operation = "subtract";
    }
    else {
        console.error("Error: Operator already selected.");
    }
}

function addMultiplication() {
    if (!operation) {
        resT.innerHTML += '*';
        operation = "multiply";
    }
    else {
        console.error("Error: Operator already selected.");
    }
}

function addDivision() {
    if (!operation) {
        resT.innerHTML += '/';
        operation = "divide";
    }
    else {
        console.error("Error: Operator already selected.");
    }
}
