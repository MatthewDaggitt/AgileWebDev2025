
let buttonPresses = 0;

function helloWorld()
{
    buttonPresses++;
    outputPresses();
}

function askForANumber() 
{
    let value = prompt("Please enter a number");
    if (value !== null)
    {
        console.log("Factorial value:" + factorial(value));
    }
}


