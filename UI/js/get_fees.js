document.getElementById('getFees').addEventListener('click', getFees);

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

    function getFees(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            fetch('http://arrotech-school-portal.herokuapp.com/api/v1/fees' ,{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let output = `<h3 style="margin-left: 10px;"> Fees grouped by Admission Number.</h3>`;
                data.fees.forEach(fee => {
                    let status = data['status'];
                    let message = data['message'];
                    const { fee_id, admission_no, transaction_type, transaction_no, description, amount } = fee
                    output += `
                        <div>
                            <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Registration No: ${fee.admission_no}</h4>
                            <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Exam ID: ${fee.fee_id}</h4>
                            <table>
                                <tr>
                                    <th>Admission No.</th>
                                    <th>Transaction Type</th>
                                    <th>Transaction Number</th>
                                    <th>Description</th>
                                    <th>Amount</th>
                                </tr>
                                <tr>
                                    <td>${fee.admission_no}</td>
                                    <td>${fee.transaction_type}</td>
                                    <td>${fee.transaction_no}</td>
                                    <td>${fee.description}</td>
                                    <td>${fee.amount}</td>
                                </tr>
                            </table>
                        </div>
                    `;
                    if (status === '200'){
                        document.getElementById('output').innerHTML = output;
                    }else{
                        raiseError(message);
                    }
                    });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }
