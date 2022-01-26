// Getting inputData from user input
var inputData=document.getElementsByTagName("input");
// Getting form elements
var Form = document.getElementsByTagName("form")[0];
// Getting message class
var message = document.getElementsByClassName("message");
function validate(){
    var fullname=inputData['fullname'].value;
    var email=inputData['email'].value;
    var phone=inputData['phone'].value;

if(email===""){
    message[0].innerText="**Please fill all the details";
  }else{
     message[0].innerText="";
  }
 
 if(phone===""){
    message[0].innerText="**Please fill all the details";
}else if(isNaN(phone)){
   message[0].innerText="*Enter Valid Phone Number";
}
else if(phone.lenght<10){
    message[0].innerText="*phone number must be ten digits"
}
else{
   message[0].innerText="";
}
if(fullname===""||email===""||phone==="" ||isNaN(phone)){
    return false;
}
return true;
}
