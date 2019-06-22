// function callToast() {
//   var x = document.getElementById("snackbar");
//   x.className = "show";
//   setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
// }
// function onSuccess(msg){
//     document.getElementById('snackbar').innerText = msg
//     callToast();
// }
// function raiseError(msg){
//     document.getElementById('snackbar').innerText = msg
//     callToast();
// }
// document.getElementById('postSignup').addEventListener('submit', postSignup);
// document.getElementById('postLogin').addEventListener('submit', postLogin);
//     function postLogin(event){
//             event.preventDefault();
//             let email = document.getElementById('email').value;
//             let password = document.getElementById('password').value;
//             fetch('http://localhost:5000/api/v1/auth/login', {
//                 method: 'POST',
//                 headers : {
//                 	Accept: 'application/json',
//                     'Content-Type': 'application/json'
//                 },
//                 body:JSON.stringify({email:email, password:password})
//             }).then((res) => res.json())
//             .then((data) =>  {
//                 console.log(data);
//                 let user = data['user'];
//                 let status = data['status'];
//                 let message = data['message'];
//                 if (status === '200'){
//                     if (user.email === 'admin@admin.com'){
//                         localStorage.setItem('token', data.token);
//                         localStorage.setItem('user', data.user);
//                         localStorage.setItem('admission_no', data.admission_no);
//                         onSuccess('Signed in successfully!');
//                         window.location.replace('admin.html');
//                     }
//                     else if (user.email === 'bursar@admin.com'){
//                         localStorage.setItem('user', data.user);
//                         localStorage.setItem('token', data.token);
//                         localStorage.setItem('admission_no', data.admission_no);
//                         onSuccess('Signed in successfully!');
//                         window.location.replace('banker.html');
//                     }
//                     else {
//                         localStorage.setItem('user', data.user);
//                         localStorage.setItem('token', data.token);
//                         localStorage.setItem('admission_no', data.admission_no);
//                         onSuccess('Signed in successfully!');
//                         window.location.replace('user.html');
//                     }
//                 }else{
//                     raiseError(message);
//                 }
//             })
//             .catch((err)=> {
//                 raiseError("Please check your internet connection!");
//                 console.log(err);
//             })
//         }
//  function postSignup(event){
//             event.preventDefault();
//
//             let firstname = document.getElementById('firstname').value;
//             let lastname = document.getElementById('lastname').value;
//             let surname = document.getElementById('surname').value;
//             let admission_no = document.getElementById('admission_no').value;
//             let email = document.getElementById('email').value;
//             let password = document.getElementById('password').value;
//             let form = document.getElementById('form').value;
//             let role = document.getElementById('role').value;
//
//             fetch('http://localhost:5000/api/v1/auth/register', {
//                 method: 'POST',
//                 headers : {
//                     Accept: 'application/json',
//                     'Content-Type': 'application/json'
//                 },
//                 body:JSON.stringify({firstname:firstname, lastname:lastname, surname:surname, admission_no:admission_no, email:email, password:password, form:form, role:role})
//             }).then((res) => res.json())
//             .then((data) =>  {
//
//                 console.log(data);
//                 let status = data['status'];
//                 let message = data['message'];
//                 if (status === '201'){
//                     localStorage.setItem("user", JSON.stringify(data[0]));
//                     localStorage.setItem('user', data.user);
//                     localStorage.setItem('admission_no', data.admission_no);
//                     window.location.replace('user.html');
//                 }else{
//                     raiseError(message);
//                 }
//             })
//             .catch((err)=>{
//                 raiseError("Please check your internet connection and try again!");
//                 console.log(err);
//             })
//         }
