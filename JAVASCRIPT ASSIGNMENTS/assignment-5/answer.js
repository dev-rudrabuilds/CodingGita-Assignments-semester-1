// Part-A] For Loop


// Question-1


// for (let i =1; i<=15 ; i++){
//     console.log(i)
// }


// Question-2

// for (let i=2; i<=40;i+=2){
//     console.log(i);
// }


// Question-3

// for (let i =1; i<=35 ; i+=2){
//     console.log(i)
// }


// Question-4

// let saving = 0;

// for (let i=0 ; i<=10 ; i++){
//     saving +=10*i
// }

// console.log("Total Saving =>" , saving)


// Question-5

// for (let i =1 ; i<=10 ; i++){
//     console.log(`12 x ${i} = ${12*i}`)
// }


// Question-6
// let glass =0;

// for (let i=1 ; i<=7 ; i++){
//     glass +=3
//     console.log(`Day ${i} : ${glass} glasses`)
// }


// Question-7


// let cost = 0;

// for (let i=1 ; i<=10 ; i++){
//     cost+=15
//     if(i==1){
//         console.log(`${i} chocolate = ₹${cost}`)
//     }
//     else{
//         console.log(`${i} chocolates = ₹${cost}`)
//     }

// }


// Question-8

// let sum = 0;

// for (let i=2 ; i<=30 ; i+=2) {
//     sum +=i
// }

// console.log("Sum of even numbers: ", sum )


// Question-9


// let count = 0;

// for (let i=1; i<=7 ; i++){
//     count+=5
//     console.log(`Day ${i}: ${count} push-ups`)
// }


// Question-10


// let ticketCost =0;

// for (let i=1 ; i<=8 ; i++){
//     ticketCost+=150
//     if(i==1){
//         console.log(`${i} person: ₹${ticketCost}`)
//     }
//     else{
//         console.log(`${i} people: ₹${ticketCost}`)
//     }
    
// }

// Question-1

// let temperature = [28, 32, 25, 40, 18, 35];
// let days = 0;

// for (let temp of temperature){
//     if(temp>30){
//         days+=1
//     }
// }

// console.log( "Number of hottest Days =>" , days)


// Question-2

// let number = 4729;
// let sum=0;

// for (;number>0 ; number=Math.floor(number/10)){
//     let digit=number%10;
//     sum=sum+digit;

// }

// console.log("Sum of digits=>" , sum);


// Question-3


// for (let i=1 ; i<=100 ; i++){
//     if(i%3==0 && i%5==0 && i%7!=0){
//         console.log(i)
//     }
// }


// Question-4

// let str1 = "JavaScript";
// let str2 = "";

// for (let consonants of str1){
//     if (consonants !== "a" && consonants !== "e" &&
//         consonants !== "i" && consonants !== "o" &&
//         consonants !== "u" && consonants !== "A" &&
//         consonants !== "E" && consonants !== "I" &&
//         consonants !== "O" && consonants !== "U")
//         {
//             str2 = str2 + consonants
//         }
// }

// console.log("Contains Only Consonants =>" , str2)



// Question-5

// let arr = [17,78,90,-5,7];
// let larger = arr[0];

// for(let i =1 ; i<=arr.length ; i++){
//     if(arr[i] > larger){
//         larger=arr[i]
//     }
// }

// console.log("largest Number=>" , larger)



// Question-6

// let num = 28;
// let sum=0;

// for(let i=1 ; i<num ; i++){
//     if(num%i==0){
//         sum+=i
//     }
// }

// if(num===sum){
//     console.log("Perfect Number.")
// }else{
//     console.log("Not a Perfect Number.")
// }


// Question-7


// for(let i=0 ; i<=7 ; i++){
//     console.log(2**i)
// }


// Question-8

// let a = 0;
// let b = 1;

// for (let i=1 ; i<=20 ; i++){
//     console.log(a);

//     let result = a + b;
//     a = b;
//     b = result;
// }




// Question-9

// let arr = [45, 78, 90, 32, 56, 88];
// let avg=0;
// let count=0;

// for (let i=0 ; i<arr.length;i++){
//     let arr1 = arr[i];
//     avg += arr1;

// }
// let average = Math.floor(avg/arr.length);

// console.log("Average Marks =>" , average)

// for(let i =0 ; i<arr.length ; i++){
//     let arr1 =arr[i];
//     if(average<arr1){
//         count+=1
//     }
// }

// console.log("Number of Students has marks above than Average Marks =>" , count)


// Question-10

// let num = 25;
// let binary = "";

// for(let n =num ; n >0 ; n = Math.floor(n/2) ){
//     let remainder = n%2;
//     binary=remainder +binary;
// }

// console.log(binary)

// Question-1

// let arr = [8 , 9 , 3 , 7 , 5 , 7 ,7];

// for (let i = 0 ; i<=arr.length ; i++ ){

//     if (arr[i] ===7){
//         console.log( "Index Number =>" , i) 
//         break
//     }
// }

// Question-2

// let password = 78692;

// for (let i=1 ; i<=5 ; i++){
//     let pass = Number(prompt("Enter Password"))
//     if(pass===password){
//         console.log("Access Granted")
//         break
//     }
// }

// console.log("Account Locked")


// Question-3

// let sum = 0;

// for(let i = 1 ; i<=100 ; i++ ){
//     if(sum>100){
//         console.log(i-1);
//         break
//     }
//     sum+=i
// }


// Question-4

// let arr = ["Nodejs" , "Html" , "Css" , "Sigma" , "JavaScript" , "Sss" ]


// for (let i=0 ; i<=arr.length ; i++){
//     let str = arr[i];
//     if(str[0] === "S"){
//         console.log(str)
//         break
//     }
// }


// Question-5


// for (let i =1 ; i<=50 ; i++){
//     if(i > 20 && Number.isInteger(Math.sqrt(i))){
//         break

//     }
//     console.log(i)
// }

// Question-1

// for (let i=1 ; i<=30 ; i++){
//     if(i %4==0){
//         continue
//     }
//     console.log(i)
// }


// Question-2


// let arr=[10, -5, 20, -8, 15, -3 ];
// let sum = 0;


// for(let i=0; i<=arr.length-1 ; i++){
    
//     if(arr[i]<0){
//         continue;
//     }
//     sum = sum  + arr[i];
// }

// console.log( "Sum of positive number =>" , sum)


// Question-3


// let str ="Hello World"; 

// for (let i =0 ; i<str.length ; i++){
//     if(str[i] ==" "){
//         continue;
//     }
//     console.log(str[i])
// }


// Question-4


// for (let i = 1 ; i<=12 ; i++){
//     if((6*i)%5===0){
//         continue;
//     }
//     console.log(6*i)
// }


// Question-5


// let arr = [12, 18, 25, 15, 30, 17, 22];

// for (let i = 0 ; i<arr.length ; i++){
//     if(arr[i]<18){
//         continue;
//     }
//     console.log(arr[i])
// }

// Question-1

// for (let i=50 ; i>=1 ; i--){
//     if (i%3 === 0 && i%9 !==0){
//         console.log(i)
//     }
// }


// Question-2


// let num = 4729;
// let product = 1;

// for (let n=num ; n>0 ; n=Math.floor(n/10)){
//     let result = (n%10)
//     if(result%2 !==0 ){
//         console.log(result)
//         product = product *result
//     }
    
// }

// console.log(product)


// Question-3


// let str = "Programming";
// let result =""

// for(let i = str.length-1 ; i>=0 ; i--){

//     let ch = str[i];

//     if (
//         ch !== "a" && ch !== "e" &&
//         ch !== "i" && ch !== "o" &&
//         ch !== "u" &&
//         ch !== "A" && ch !== "E" &&
//         ch !== "I" && ch !== "O" &&
//         ch !== "U"
//     ) {
//         result = result + ch;
//     }
    
// }
// console.log(result)



// Question-4

// let a = 0;
// let b = 1;
// let c;

// for (let i = 1; i <= 15; i++) {
//     c = a + b;
//     a = b;
//     b = c;
// }

// for (let i = 1; i <= 15; i++) {
//     c = b - a;
//     console.log(c);
//     b = a;
//     a = c;
// }


// Question-5


// let num =747;

// let reverse =0;

// for(let n = num ; n>0 ; n=Math.floor(n/10)){
//     let result = n%10;
//     reverse = reverse*10 + result;
// }
// if(reverse===num){
//     console.log("Palindrome Number");
    
// }
// else{
//     console.log("Not a Palindrome Number");

// }


// Question-6

// let arr = [12, 45, 7, 23, 56, 89, 34];

// let greater = arr[0];

// for (let i = arr.length-1 ; i>=0 ; i-- ){

//     if(arr[i]<50 && arr[i]>greater){

//         greater=arr[i]
//     }
// }

// console.log(greater)


// Question-7


// let temp = [32, 28, 41, 19, 35, 27, 38];

// let count = 0;

// for(let i = temp.length-1 ; i>=0 ; i--){

//     if(temp[i] < 30 ){
//         count+=1
//     }
// }
// console.log("Days Colder Than 30 degree =>" , count)


// Question-8

// let num =13 ;

// let binary = "";

// for(let n=num ; n>0 ; n = Math.floor(n/2)){
//     let remainder = n%2;
//     binary = binary + remainder;

// }

// console.log(binary)


// Question-9


// let arr = [90, 85, 70, 95, 60, 88, 75];

// for(let i=arr.length-1 ; i>=0 ; i--){

//     if(arr[i] > 80){
//         console.log("Score =>" , arr[i])
//         console.log("Score Index =>" , i)
//         break;
//     }
// }


// Question-10


// for(let i =40 ; i>=0 ; i--){

//     if(Number.isInteger(Math.sqrt(i))){
//         continue;
//     }
//     else{
//         console.log(i)
//     }
// }

// Question-1

// let num =1

// for(let i =1 ; i<=4 ; i++){
//     let row = ""
//     for (let j =1 ; j<=i ; j++){
//         row =row + num+" ";
//         num++;
//     }
//     console.log(row);
// }


// Question-2

// let num =1;

// for(let i = 1 ; i<=4 ; i++){
//     let row = "";
//     for(let j = 1 ; j<=i ; j++){
//         row = row + num + " ";

//     }
//     console.log(row);
//     num++;
// }


// Question-3

// let num =1

// for(let i =1 ; i<=4 ; i++){
//     let row = ""
//     for (let j =1 ; j<=i ; j++){
//         row =row + num+" ";
//         num++;
//     }
//     console.log(row);
// }


// Question-4

// for(let i=1 ; i<=4 ; i++){
//     let row = ""
//     for(let j=1 ; j<=4 ; j++){
//         if(i===1 || i===4 || j===1 || j===4){
//             row = row + "* "

//         }
//         else{
//             row = row + "  "

//         }

//     }
    
//     console.log(row)

// }


// Question-5


// for(let i =1 ; i<=6 ; i++){
//     let row = "";
//     for(let j =1 ; j<=i ; j++){
//         if(i%2===0){
//             row =row + "$ "
//         }
//         else{
//             row =row + "# "
//         }
//     }
//     console.log(row)

// }


// Question-6


// for (let i=1 ; i<=5 ; i++){
//     let row = "";
//     for (let j=1 ; j<=i ; j++){
//         row =row + String.fromCharCode((64+j)) + " " ;
        
//     }
//     console.log(row);

// }


// Question-7


// for (let i =1 ; i<=5 ; i++){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         if(i===5 || j===1 || j===i){
//             row =row + "* "
//         }
//         else{
//             row = row + "  "
//         }
//     }
//     console.log(row)
// }


// Question-8


// for (let i =5 ; i>=1 ; i--){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         row =row + "*"
//     }
//     console.log(row)
// }


// Question-9


// for (let i =5 ; i>=1 ; i--){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         row =row + i + " "
//     }
//     console.log(row)
// }


// Question-10


// for (let i =5 ; i>=1 ; i--){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         row =row + j + " "
//     }
//     console.log(row)
// }


// Question-11

// let num =15

// for (let i =5 ; i>=1 ; i--){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         row =row + num + " "
//         num--;
//     }
//     console.log(row)
// }


// Question-12


// for (let i=5 ; i>=1 ;i--){
//     let row = "";
//     for (let j =1 ; j<=i ; j++){
//         if(i===5 || j===1 || j==i){
//             row =row+"* "

//         }
//         else{
//             row = row +"  ";
//         }
//     }
//     console.log(row);
// }


// Question-13

// let row =5;
// let col =5;

// for (let i=1 ; i<=row ;i++){
//     let bag = "";
//     for (let j =1 ; j<=col ; j++){
//         if(j==i){
//             bag =bag+"  "

//         }
//         else{
//             bag = bag +"* ";
//         }
//     }
//     console.log(bag);
// }


// Question-14


// for(let i = 1 ; i<=5 ; i++){
//     let row = "";
//     for(let j = 1 ; j<=10 ; j++){
//         if(i*j%2===0){
//             row = row + `${i * j} `                
//         }
        

//     }
//     console.log(`Table = ${i} => ${row}`)


// }


// Question-15

// let row =3;

// for(let i =1 ;i<=row ; i++){
//     let bag = "";
//     for(let j =1 ;j<=row-i ; j++){
//         bag = bag + "  ";

//     }
//     for(let k =1 ;k<=i ; k++){
//         bag = bag + k + " ";

//     }
//     for(let l =i-1 ;l>=1 ; l--){
//         bag = bag + l + " ";

//     }
//     console.log(bag)
// }

// Question-1

// let num = 1;

// while(num<=10){
//     console.log(num);
//     num++;
// }


// Question-2


// let i = 1;

// let sum =0;

// while(i<=10){
//     sum+=i;
//     i++;

// }
// console.log(sum)


// Question-3

// let num = 7;

// let i=1;

// while(i<=10){
//     console.log(`7 x ${i} => ${7*i}`);
//     i++;
// }


// Question-4


// let num =58786;
// let count=0;

// while(num!=0){
//     num = Math.floor(num/10);
//     count+=1;
// }
// console.log(count)


// Question-5


// let num = 12345;
// let newNum = "";

// while(num!=0){
//     newNum = newNum + num%10;
//     num = Math.floor(num/10);

// }
// console.log(newNum)


// Question-6


// let num =4729;
// let total =0;

// while(num!=0){
//     total += num%10;
//     num=Math.floor(num/10);

// }
// console.log(total)


// Question-7

// let num =1;

// while(num<=100){
//     if(num % 3==0 && num % 5==0 && num % 7 !=0){
//         console.log(num)
//     }
//     num++
// }


// Question-8

// let num = 5;
// let fact = 1;

// while(num >=1){
//     fact *=num;
//     num--
// }
// console.log(fact)


// Question-9

// let num = 747;
// let original=num;
// let drome = "";

// while(num!=0){
//     drome = drome + num%10;
//     num = Math.floor(num/10);
// }

// if(Number(drome) === original){
//     console.log("Palindrome Number");
// }
// else{
//     console.log("Not a Palindrome Number");
// }


// Question-10

// let  num = 13;

// let result = ""

// while (num!=0){
//     result =  num%2 + result;
//     num = Math.floor(num/2);

// }
// console.log(result)

// Question-1


// let num = 10 ;

// do {
//     console.log(num)
//     num--
// }while(num>=1)


// Question-2

// let num = 1;

// do{
//     if(num%2==0){
//         console.log(num)
//     }
//     num++
// }while(num<=20)


// Question-3

// let num =5;
// let sum =0;

// do{
//     if(num>=1){
//         sum+=num;
//     }
//     num--;
// }while(num>=1)
// console.log(sum)


// Question-4

// let num =234;
// let product = 1;

// do{
//     let newNum = num%10;
//     product *=newNum
//     num = Math.floor(num/10)
// }while (num!=0)
// console.log(product)


// Question-5

// let num =58372;
// let newNum =0;



// do{
//     newNum = num%10
//     num = Math.floor(num/10)
// }while (num!=0)
// console.log(newNum)


// Question-6

// let base =3;
// let result=1;
// let exponent=4;
// let i=1;

// do{
//     result *=base
//     i+=1

// }while(i<=exponent)

// console.log(result)


// Question-7


// let num=1;

// do{
//     if(num%4==0 && num%8==0){
//         console.log(num);
//     }
//     num++;
// }while(num<=100)


// Question-8

// let num =1221;
// let originalNum = num;
// let reversedNum =0
// let digit

// do{
//     digit=num%10
//     reversedNum = reversedNum*10 + digit;
//     num = Math.floor(num/10)

// }while(num!=0)

// if(originalNum ==reversedNum){
//     console.log("Palindrome Number")
// }
// else{
//     console.log("Not a Palindrome Number")
// }


// Question-9

// let num1 = 48;
// let num2 = 18;
// let remainder;

// do{
//     remainder = num1 % num2;
//     num1 = num2;
//     num2=remainder
// }while(num2!=0)
    
// console.log("GDC" , num1)
    
    

// Question-10


// let num =13;
// let binary="";

// do{
//     binary =  num%2 + binary
//     num = Math.floor(num/2)
// }while(num!=0)

// console.log(binary)