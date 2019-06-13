document.getElementById('studentLogin').addEventListener('submit', studentLogin);

    function callToast() {

      var x = document.getElementById("snackbar");
      x.className = "show";
      setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
    }

    function onSuccess(msg){

        document.getElementById('snackbar').innerText = msg
        callToast();
    }

    function raiseError(msg){

        document.getElementById('snackbar').innerText = msg
        callToast();
    }

    function studentLogin(event){
            event.preventDefault();

            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;

            fetch('https://arrotech-school-portal.herokuapp.com/api/v1/auth/login', {
                method: 'POST',
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({email:email, password:password})
            }).then((res) => res.json())
            .then((data) =>  {

                console.log(data);
                let user = data['user'];
                let status = data['status'];
                let message = data['message'];
                if (status === '200'){
                    if (user.email != 'admin@admin.com' || user.email != 'bursar@admin.com'){
                        localStorage.setItem('token', data.token);
                        localStorage.setItem('user', data.user);
                        localStorage.setItem('admission_no', data.admission_no);
                        onSuccess('Signed in successfully!');
                        window.location.replace('user.html');
                    }
                    else{
                    localStorage.setItem('token', data.token);
                    onSuccess('You are not authorized!');
                    window.location.replace('student_login.html');
                    }
                }else{
                    raiseError(message);
                }

            })
            .catch((err)=> {
                raiseError("Please check your internet connection!");
                console.log(err);
            })
        }
