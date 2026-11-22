// Question-1

// function displayCourse(){
//     return ("JavaScript Fundamentals")
// }
// console.log(displayCourse())

// Question-2

// function getStudentStatus(){
//     return ("Active Learner")
// }
// let result = getStudentStatus()
// console.log(result)

// Question-3

// console.log(getStudentStatus())

// function getStudentStatus(){
//     return ("Active Learner")
// }

// Question-1

// let showMotto = function(){
//     return ("Code. Learn. Grow.")
// }
// console.log(showMotto())

// Question-2

// let getSemester = function(){
//     return (3)
// }
// console.log(getSemester())


// Question-3

// console.log(getSemester())

// let getSemester = function(){
//     return (3)
// }

// Question-1

// let showMotto = function(){
//     return ("Code. Learn. Grow.")
// }
// console.log(showMotto())

// Question-2

// let getSemester = function(){
//     return (3)
// }
// console.log(getSemester())


// Question-3

// console.log(getSemester())

// let getSemester = function(){
//     return (3)
// }

// Question-1

// function subtract(a ,b){
//     return (a-b)
// }
// console.log(subtract(50 , 18))

// Question-2

// let greetUser = function(name){
//     console.log(`Welcome, ${name}! `)
// }
// greetUser("Faiyaz")


// Question-3

// function calculateArea(length, breadth){
//     return (length * breadth)
// }
// console.log(calculateArea(12 , 5))
// console.log(calculateArea(8 , 9))

// Theory Questions
// Question-4. Difference between Parameter and Argument
// - Parameter: A variable written inside the function definition.
// - Argument: The actual value passed when calling the function.
// Example:
// function greet(name) {  // name is parameter
//     console.log(name);
// }

// greet("Aarav");  // "Aarav" is argument


// Question-5. Can a function have parameters but be called without arguments?

// Yes. In that case, the parameters get the value undefined by default (if no default value is provided).

// Example:
// function greet(name) {
//     console.log(name);
// }

// greet(); // undefined

// Question-1


// function sqaureOfNumber(n){
//     return (n**2)
// }
// console.log(sqaureOfNumber(9))


// Question-2

// function isAdult(age){
//     if (age>=18){
//         return (true)
//     }else{
//         return (false)
//     }
// }
// console.log(isAdult(17))
// console.log(isAdult(20))


// Question-3

// function getFullName(firstName , LastName){
//     return (firstName + LastName)
// }
// console.log("Rohit" , "Sharma")

// Theory Questions 
// Question-4. What does a function return if there is no return statement?

// A function returns undefined if there is no return statement.

// Question-5. Why do we use return instead of console.log()?

// return sends a value back from the function so it can be stored or used in other calculations. console.log() only displays the value on the console and does not return it.

// Question-1

// function getTotal(m1 , m2 , m3){
//     let totaMarks = m1+m2+m3
//     return (`The TotalMarks is ${totaMarks}`)
// }
// console.log(getTotal(90 , 91 , 95))
// console.log(getTotal(80, 75 , 58))


// Question-2

// function calculateSimpleInterest(principal , rate , time){
//     return (`Simple Interest ${principal * rate * time}`)
// }

// console.log(calculateSimpleInterest(25 , 5 ,6))
// console.log(calculateSimpleInterest(15 , 3 ,2))


// Question-3
 
//student -1

// let maths = 98;
// let physics = 95;
// let chemisttry =90;

// let avgMarks = ((maths + physics + chemisttry)/3).toFixed(2)
// console.log("Average Marks of a Student =>" , avgMarks)

// // student -2

// let maths1 = 90;
// let physics1 = 55;
// let chemisttry1 =80;

// let avgMarks1 = ((maths1 + physics1 + chemisttry1)/3).toFixed(2)
// console.log("Average Marks of a Student =>" , avgMarks1)

//using Function

// function findAverage(a,b,c){
//     let avgMarks = ((a + b + c)/3).toFixed(2) 

//     return (`Average Marks of Student => ${avgMarks}`)

// }
// console.log(findAverage(90 , 85 , 96))
// console.log(findAverage(50 , 75 , 58))


// Theory Questions – 3
// Question-4. How do functions help in reducing code repetition?

// Functions allow us to write code once and use it multiple times by calling the function.

// Example: A calculator function can be used to add different numbers without writing the addition code again and again.

// Question-5. Mention any three advantages of using functions in a program.
// 1. Reduces code repetition.
// 2. Makes code easier to understand.
// 3. Makes code reusable and easier to maintain.

// Question-1

// function showCity() {
//     let city = "Ahmedabad";
//     console.log(city);
// }

// showCity();
// console.log(city); // Error: city is not defined

// Question-2
// let trainer = "CodingGita Mentor";

// function displayTrainer() {
//     console.log(trainer);
// }

// displayTrainer();
// console.log(trainer);

// Question-3
// function demoScope() {
//     let value = 50;
//     console.log(value);
// }

// demoScope();

// console.log(value); // Error: value is not defined


// Theory Questions
// Question-4

// JavaScript follows function scope to protect local variables from being accessed outside the function. It helps prevent unwanted changes, naming conflicts and errors.

// Question-5

// If a global and local variable have the same name, the function uses the local variable because it has priority inside that function.

// Practical Questions
// Question-1
// function generateMessage(name, score) {
//     if (score >= 40) {
//         return name + " has scored " + score + " and the result is Pass";
//     } else {
//         return name + " has scored " + score + " and the result is Fail";
//     }
// }

// console.log(generateMessage("Aarav", 65));


// Question-2
// function billCalculator(item1, item2, item3) {
//     let total = item1 + item2 + item3;

//     if (total >= 1000) {
//         return "Total = " + total + ", Discount Applied";
//     } else {
//         return "Total = " + total + ", No Discount";
//     }
// }

// console.log(billCalculator(400, 300, 500));


// Question-3
// function performanceReport(student, m1, m2, m3) {
//     let total = m1 + m2 + m3;
//     let average = total / 3;
//     let remark;

//     if (average >= 80) {
//         remark = "Excellent";
//     } else {
//         remark = "Keep Improving";
//     }

//     return "Name: " + student +
//            ", Total: " + total +
//            ", Average: " + average +
//            ", Remark: " + remark;
// }

// console.log(performanceReport("Aarav", 85, 90, 80));


// Theory Questions
// Question-4

// It is better to perform related tasks inside one function because the code becomes organized, reusable and easier to understand. It also reduces code repetition.

// Question-5

// Combining parameters, return and conditions inside one function makes code more reusable, flexible, readable and efficient.

// Question-1
// function mainTask() {
//     function helperTask() {
//         return "Task completed successfully";
//     }

//     return helperTask();
// }

// console.log(mainTask());


// Question-2
// function calculateFinal(m1, m2) {
//     function getTotal() {
//         return m1 + m2;
//     }

//     return "Final marks = " + getTotal();
// }

// console.log(calculateFinal(80, 90));


// Question-3
// function studentStatus(name, marks) {
//     function getGrade() {
//         if (marks >= 80) {
//             return "A";
//         } else if (marks >= 60) {
//             return "B";
//         } else {
//             return "C";
//         }
//     }

//     return name + " has received grade " + getGrade();
// }

// console.log(studentStatus("Aarav", 85));


// Theory Questions
// Question-4

// The main advantage of nested functions is that they keep helper functions private and organize related code. We use them when a function is needed only inside another function.

// Question-5

// Yes, an inner function can access variables of its outer function because of lexical scope. But the outer function cannot directly access variables declared inside the inner function.
// =================================================================

// Question-1
// var city = "Surat";

// function display() {
//     var country = "India";

//     console.log(city);
//     console.log(country);
// }

// display();

// Global variable: city
// Function-scoped variable: country
// Both are accessible inside display()


// Question-2
// var price = 500;

// function calculate() {
//     var tax = 50;
//     console.log(price + tax);
// }

// calculate();
// console.log(price);

// Output:
// 550
// 500


// Question-3
// var college = "ABC College";

// function student() {
//     var name = "Rahul";
//     var age = 20;
// }

// function teacher() {
//     var subject = "JavaScript";
// }

// college = Global scope
// name = Function scope
// age = Function scope
// subject = Function scope


// Question-4
// function first() {
//     var number = 100;
// }

// function second() {
//     console.log(number);
// }

// first();
// second();

// Output:
// ReferenceError: number is not defined
// number is local to first()


// Question-5
// var globalValue = 100;

// function showValues() {
//     var localValue = 50;

//     console.log(globalValue);
//     console.log(localValue);
// }

// showValues();
// console.log(globalValue);

// Output:
// 100
// 50
// 100

// Question-6
// var game = "Cricket";

// function play() {
//     console.log("I like " + game);
// }

// play();
// console.log(game);

// Output:
// I like Cricket
// Cricket


// Question-7
// var language = "English";

// function showLanguage() {
//     console.log(language);
// }

// function changeLanguage() {
//     language = "Gujarati";
// }

// showLanguage();
// changeLanguage();
// showLanguage();
// console.log(language);

// Output:
// English
// Gujarati
// Gujarati


// Question-8
// function displayMarks() {
//     console.log(marks);
// }

// var marks = 75;

// displayMarks();

// Output:
// 75
// No error because marks is declared globally before the function is called.


// Question-9
// var color = "Red";

// function showColor() {
//     var message = "Favorite color: ";
//     console.log(message + color);
// }

// showColor();
// console.log(color);

// Output:
// Favorite color: Red
// Red

// console.log(message);
// ReferenceError: message is not defined


// Question-10
// var school = "Sunrise School";

// function showSchool() {
//     console.log(school);
// }

// function updateSchool() {
//     school = "Green Valley School";
// }

// showSchool();
// updateSchool();
// showSchool();

// console.log(school);

// Output:
// Sunrise School
// Green Valley School
// Green Valley School

// Question-11
// function calculateTotal() {
//     var first = 100;
//     var second = 200;

//     console.log(first + second);
// }

// calculateTotal();

// // console.log(first);
// // ReferenceError: first is not defined

// // Output:
// // 300


// Question-12
// function employee() {
//     var salary = 30000;
// }

// employee();

// // console.log(salary);
// // ReferenceError: salary is not defined


// Question-13
// var number = 15;

// function test() {
//     var number = 25;
//     console.log(number);
// }

// test();
// console.log(number);

// // Output:
// // 25
// // 15


// Question-14
// function calculate() {
//     var result = 40;
//     result = result + 10;

//     console.log(result);
// }

// calculate();
// calculate();

// // Output:
// // 50
// // 50

// // A new local variable is created on each function call.
// // It is not accessible after the function finishes.


// Question-15
// function calculateArea() {
//     var length = 8;
//     var width = 4;

//     var area = length * width;

//     console.log("Area =", area);
// }

// calculateArea();

// // Output:
// // Area = 32

// Question-16
// if (10 > 5) {
//     var result = "Success";
// }

// console.log(result);

// // Output:
// // Success
// // var does not have block scope.


// Question-17
// var number = 1;

// if (true) {
//     var number = 2;
// }

// console.log(number);

// // Output:
// // 2
// // Both declarations refer to the same variable.


// Question-18
// var message = "Start";

// {
//     var message = "End";
// }

// console.log(message);

// // Output:
// // End
// // A normal block does not create a separate scope for var.


// Question-19
// if (false) {
//     var result = 100;
// }

// console.log(result);

// // Output:
// // undefined
// // var is hoisted, but the assignment is not executed.


// Question-20
// if (true) {
//     let secret = "Hidden";
// }

// // console.log(secret);
// // ReferenceError: secret is not defined

// // let provides block scope, so secret cannot be accessed outside the if block.

// Question-21
// for (var number = 2; number <= 6; number += 2) {
//     console.log(number);
// }

// console.log("Final:", number);

// // Output:
// // 2
// // 4
// // 6
// // Final: 8


// Question-22
// var count = 10;

// for (var count = 1; count <= 3; count++) {
//     console.log(count);
// }

// console.log("Count:", count);

// // Output:
// // 1
// // 2
// // 3
// // Count: 4

// // The original value 10 is replaced because var has no block scope.


// Question-23
// var i = 5;

// while (i > 2) {
//     console.log(i);
//     i--;
// }

// console.log("After loop:", i);

// // Output:
// // 5
// // 4
// // 3
// // After loop: 2

// // i is accessible after the loop because it is declared using var.


// Question-24
// for (var item = 1; item <= 3; item++) {
//     console.log("Item:", item);
// }

// console.log("Last item:", item);

// // Output:
// // Item: 1
// // Item: 2
// // Item: 3
// // Last item: 4

// // No error because var is accessible outside the loop.


// Question-25
// for (let step = 1; step <= 4; step++) {
//     console.log(step);
// }

// // console.log(step);
// // ReferenceError: step is not defined

// // let provides block scope, so step cannot be accessed outside the loop.

// Question-26
// function calculate() {
//     for (var number = 1; number <= 3; number++) {
//         console.log(number * 10);
//     }

//     console.log("Final:", number);
// }

// calculate();

// // Output:
// // 10
// // 20
// // 30
// // Final: 4

// // number is accessible inside the function but not outside it.


// Question-27
// function student() {
//     for (var marks = 60; marks <= 80; marks += 10) {
//         console.log(marks);
//     }

//     console.log(marks);
// }

// student();

// // console.log(marks);
// // ReferenceError: marks is not defined

// // Output:
// // 60
// // 70
// // 80
// // 90

// // The first four uses are valid.
// // The last statement outside the function causes an error.


// Question-28
// function test() {
//     var value = 5;

//     while (value < 8) {
//         console.log(value);
//         value++;
//     }

//     console.log("Final value:", value);
// }

// test();

// // Output:
// // 5
// // 6
// // 7
// // Final value: 8

// // Loop executes 3 times.


// Question-29
// function calculate() {
//     for (var i = 1; i <= 2; i++) {
//         console.log(i);
//     }
// }

// // console.log(i);
// // ReferenceError: i is not defined

// calculate();

// // Output:
// // 1
// // 2

// // i is local to calculate(), so it cannot be accessed outside.


// Question-30
// function printNumbers() {
//     for (var i = 1; i <= 5; i++) {
//         console.log(i);
//     }

//     console.log("Final:", i);
// }

// printNumbers();

// // console.log(i);
// // ReferenceError: i is not defined

// // Output:
// // 1
// // 2
// // 3
// // 4
// // 5
// // Final: 6

// // var is function-scoped, so i is accessible inside the function only.

// Question-31
// console.log(score);

// var score = 90;

// console.log(score);

// // Output:
// // undefined
// // 90

// // var declaration is hoisted and initialized with undefined.


// Question-32
// var a = 10;

// function test() {
//     console.log(a);

//     var a = 20;

//     console.log(a);
// }

// test();

// // Output:
// // undefined
// // 20

// // Local a is hoisted, so it does not use the global value.


// Question-33
// console.log(first);
// console.log(second);

// var first = 100;
// var second = 200;

// console.log(first);
// console.log(second);

// // Output:
// // undefined
// // undefined
// // 100
// // 200


// Question-34
// function calculate() {
//     console.log(total);

//     var total = 50;

//     console.log(total);
// }

// calculate();

// // Output:
// // undefined
// // 50

// // Hoisting works like this:

// function calculateExample() {
//     var total;
//     console.log(total);

//     total = 50;
//     console.log(total);
// }

// calculateExample();


// Question-35
// var price = 100;

// function showPrice() {
//     console.log(price);

//     var price = 500;
// }

// showPrice();
// console.log(price);

// // Output:
// // undefined
// // 100

// // Local price is hoisted inside the function.
// // It does not use the global price.

// Question-36
// sayHello();

// function sayHello() {
//     console.log("Hello from CodingGita");
// }

// // Output:
// // Hello from CodingGita

// // Function declarations are completely hoisted.


// Question-37
// display();

// function display() {
//     console.log("Function is hoisted completely");
// }

// // Output:
// // Function is hoisted completely

// // Unlike var, the complete function is available before declaration.


// Question-38
// greet();

// // Output:
// // TypeError: greet is not a function

// var greet = function() {
//     console.log("Hi");
// };

// // var is hoisted as undefined, but the function assignment is not hoisted.


// Question-39
// console.log(typeof myFunc);

// function myFunc() {
//     return "I am hoisted";
// }

// console.log(myFunc());

// // Output:
// // function
// // I am hoisted


// Question-40
// var name = "Rahul";

// showMessage();

// function showMessage() {
//     console.log("Hello " + name);
// }

// // Output:
// // Hello Rahul

// // The function can be called before its declaration because of hoisting.

// Question-41
// var institute = "CodingGita";

// function department() {
//     var dept = "CSE";

//     function batch() {
//         var year = 2025;

//         console.log(year);
//         console.log(dept);
//         console.log(institute);
//     }

//     batch();
// }

// department();

// // Output:
// // 2025
// // CSE
// // CodingGita

// // JavaScript searches the local scope first,
// // then outer scope, then global scope.


// Question-42
// var globalVar = "I am global";

// function outer() {
//     var outerVar = "I am outer";

//     function inner() {
//         console.log(globalVar);
//         console.log(outerVar);
//         console.log(innerVar);
//     }

//     inner();
// }

// outer();

// // Output:
// // I am global
// // I am outer
// // ReferenceError: innerVar is not defined

// // innerVar is not declared in any accessible scope.


// Question-43
// var a = 1;

// function level1() {
//     var b = 2;

//     function level2() {
//         var c = 3;

//         function deep() {
//             console.log(a, b, c);
//         }

//         deep();
//     }

//     level2();
// }

// level1();

// // Output:
// // 1 2 3

// // deep() can access a, b and c through the scope chain.


// Question-44
// var x = "global";

// function first() {
//     var x = "first";

//     function second() {
//         console.log(x);
//     }

//     second();
// }

// first();
// console.log(x);

// // Output:
// // first
// // global

// // Inside second(), JavaScript uses the nearest x variable.
// // Outside the function, it uses the global x.


// Question-45
// var a = "Global Variable";

// function outer() {
//     var b = "Outer Variable";

//     function middle() {
//         var c = "Middle Variable";

//         function inner() {
//             var d = "Inner Variable";

//             console.log(d);
//             console.log(c);
//             console.log(b);
//             console.log(a);
//         }

//         inner();
//     }

//     middle();
// }

// outer();

// // Output:
// // Inner Variable
// // Middle Variable
// // Outer Variable
// // Global Variable

// Question-46
// var score = 50;

// function test() {
//     var score = 90;
//     console.log(score);
// }

// test();
// console.log(score);

// // Output:
// // 90
// // 50

// // Shadowing means a local variable has the same name as a global variable.


// Question-47
// var name = "Global Name";

// function show() {
//     var name = "Local Name";
//     console.log(name);
// }

// show();
// console.log(name);

// // Output:
// // Local Name
// // Global Name

// // Local name does not change the global variable.


// Question-48
// var value = 10;

// function update() {
//     value = 20;
//     console.log(value);
// }

// update();
// console.log(value);

// // Output:
// // 20
// // 20

// // Without var, the existing global variable is updated.


// Question-49
// var color = "Blue";

// function changeColor() {
//     var color = "Red";
//     console.log("Inside:", color);
// }

// changeColor();
// console.log("Outside:", color);

// // Output:
// // Inside: Red
// // Outside: Blue


// Question-50
// var marks = 70;

// function showMarks() {
//     var marks = 95;
//     console.log("Inside:", marks);
// }

// showMarks();

// console.log("Outside:", marks);

// // Output:
// // Inside: 95
// // Outside: 70

// Question-51
// function outer() {
//     var teacher = "Kartik Sir";

//     function inner() {
//         var student = "Jenil";

//         console.log(student);
//         console.log(teacher);
//     }

//     inner();
// }

// outer();

// // Output:
// // Jenil
// // Kartik Sir

// // teacher and student cannot be accessed directly outside outer().


// Question-52
// function parent() {
//     var a = "Parent";

//     function child() {
//         var b = "Child";

//         function grandchild() {
//             var c = "Grandchild";

//             console.log(a);
//             console.log(b);
//             console.log(c);
//         }

//         grandchild();
//     }

//     child();
// }

// parent();

// // Output:
// // Parent
// // Child
// // Grandchild


// Question-53
// function outer() {
//     var secret = "Hidden";

//     function inner() {
//         console.log(secret);
//     }
// }

// // inner();
// // ReferenceError: inner is not defined

// outer();

// // Error occurs because inner() is declared inside outer()
// // and cannot be called directly outside it.


// Question-54
// function createMessage() {
//     var greeting = "Hello";

//     function show() {
//         console.log(greeting + " students");
//     }

//     return show;
// }

// var messageFunc = createMessage();

// messageFunc();

// // Output:
// // Hello students

// // The inner function remembers the outer variable greeting.
// // This is called a closure.


// Question-55
// function studentInfo() {
//     var name = "Rahul";
//     var course = "JavaScript";

//     function display() {
//         console.log("Name:", name);
//         console.log("Course:", course);
//     }

//     display();
// }

// studentInfo();

// // Output:
// // Name: Rahul
// // Course: JavaScript

// Question-56
// function test() {
//     x = 100;
// }

// test();

// console.log(x);

// // Output in a non-strict classic script:
// // 100

// // Problem: x is created as a global variable accidentally.
// // In strict mode, this causes a ReferenceError.


// Question-57
// if (true) {
//     var x = 20;
// }

// console.log(x);

// // Output:
// // 20

// // var does not have block scope.
// // Therefore, x is accessible outside the if block.


// Question-58
// console.log(a);

// var a = 10;

// // Output:
// // undefined

// // var declaration is hoisted to the top of its scope.


// Question-59
// var x = 10;

// var x = 20;

// console.log(x);

// // Output:
// // 20

// // var allows redeclaration.
// // It can become confusing because the previous value is overwritten.


// Question-60
// function calculate() {
//     var total = 0;

//     for (var i = 1; i <= 5; i++) {
//         total = total + i;
//     }

//     console.log(total);
// }

// calculate();

// // console.log(total);
// // ReferenceError: total is not defined

// // Output:
// // 15

// // total is declared inside the function.
// // It cannot be accessed outside the function.