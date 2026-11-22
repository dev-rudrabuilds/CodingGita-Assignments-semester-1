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