document.getElementById('updateFees').addEventListener('submit', updateFees);

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

    function updateFees(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');


            let admission_no = document.getElementById('admission_no').value;
            let transaction_type = document.getElementById('transaction_type').value;
            let transaction_no = document.getElementById('transaction_no').value;
            let description = document.getElementById('description').value;
            let amount = document.getElementById('amount').value;


            fetch('http://localhost:5000/api/v1/fees/' + admission_no, {
                method: 'PUT',
                path: admission_no,
                headers : {
                	Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
                body:JSON.stringify({admission_no:admission_no, transaction_type:transaction_type, transaction_no:transaction_no, description:description, amount:amount})
            }).then((res) => res.json())
            .then((data) =>  {

                console.log(data);
                let status = data['status'];
                let message = data['message'];
                if (status === '200'){
                    onSuccess('Fees updated successfully!');
                }else{
                    raiseError(message);
                }

            })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
        }
