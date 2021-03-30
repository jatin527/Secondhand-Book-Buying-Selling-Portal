function validate(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;
    if(username=="Capstone" && password=="Capstone"){
        alert("Login Successful")
        return false;
    } 
    else{
        alert("login failed")
    }
}