# Calculator
Ex.No:06 JavaScript Calculator

Date: 26.11.2026

AIM:

To design and develop a simple calculator using HTML, CSS, and JavaScript to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

ALGORITHM:

Create an HTML page to design the calculator interface.
Create a display field to show the numbers and calculation results.
Create buttons for digits from 0 to 9 and arithmetic operators.
Use CSS to arrange and style the calculator buttons and display.
Write JavaScript functions to handle button clicks.
Store the entered numbers and operators in the calculator display.
Use JavaScript to evaluate the arithmetic expression.
Display the calculated result on the calculator screen.
Provide a clear button to reset the calculator.
Test the calculator with different arithmetic operations.

PROGRAM:
'''
<!DOCTYPE html>
<html>
<head>
  <title>Calculator</title>
  <style>
    body {
      text-align: center;
      font-family: Arial;
    }

    #display {
      width: 220px;
      height: 40px;
      font-size: 20px;
      text-align: right;
      margin-bottom: 10px;
    }

    button {
      width: 50px;
      height: 50px;
      font-size: 18px;
      margin: 3px;
    }
  </style>
</head>
<body>

  <h2>Simple Calculator</h2>

  <input type="text" id="display" readonly>
  <br>

  <button onclick="add('7')">7</button>
  <button onclick="add('8')">8</button>
  <button onclick="add('9')">9</button>
  <button onclick="add('/')">/</button>
  <br>

  <button onclick="add('4')">4</button>
  <button onclick="add('5')">5</button>
  <button onclick="add('6')">6</button>
  <button onclick="add('*')">*</button>
  <br>

  <button onclick="add('1')">1</button>
  <button onclick="add('2')">2</button>
  <button onclick="add('3')">3</button>
  <button onclick="add('-')">-</button>
  <br>

  <button onclick="add('0')">0</button>
  <button onclick="add('.')">.</button>
  <button onclick="calculate()">=</button>
  <button onclick="add('+')">+</button>
  <br>

  <button onclick="clearDisplay()">C</button>

  <script>
    function add(value) {
      document.getElementById("display").value += value;
    }

    function clearDisplay() {
      document.getElementById("display").value = "";
    }

    function calculate() {
      try {
        var result = eval(document.getElementById("display").value);
        document.getElementById("display").value = result;
      } catch (error) {
        document.getElementById("display").value = "Error";
      }
    }
  </script>

</body>
</html>
'''

OUTPUT:

![alt text](image.png)


RESULT
Thus, a JavaScript-based calculator was successfully designed and developed to perform basic arithmetic operations using HTML, CSS, and JavaScript.
