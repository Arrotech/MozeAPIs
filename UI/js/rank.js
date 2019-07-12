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

document.getElementById('mybtn').onclick = () => {
        event.preventDefault();

        token = window.localStorage.getItem('token');
        admission = window.localStorage.getItem('admission_no');

        fetch('http://localhost:5000/api/v1/exams/' + admission, {
            method: 'GET',
            path: admission,
            headers : {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        })
        .then((res) => res.json())
        .then((data) => {
          data.Exam.forEach(exam => {
                let status = data['status'];
                let message = data['message'];
                console.log(message);
                console.log(data);
                console.log(status);
                const { admission_no, term, form, type, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business, total } = exam;
                rank += `
                    <div>
                        <table>
                            <tr>
                                // <th>Admission No.</th>
                                <th>Term</th>
                                <th>Form</th>
                                <th>Type</th>
                                <th>Mathematics</th>
                                <th>English</th>
                                <th>Kiswahili</th>
                                <th>Chemistry</th>
                                <th>Biology</th>
                                <th>Physics</th>
                                <th>History</th>
                                <th>Geography</th>
                                <th>Cre</th>
                                <th>Agriculture</th>
                                <th>Business</th>
                                <th>Total</th>
                            </tr>
                            <tr>
                                <td>${data.exam.admission_no}</td>
                                <td>${data.exam.term}</td>
                                <td>${data.exam.form}</td>
                                <td>${data.exam.type}</td>
                                <td>${data.exam.maths}</td>
                                <td>${data.exam.english}</td>
                                <td>${data.exam.kiswahili}</td>
                                <td>${data.exam.chemistry}</td>
                                <td>${data.exam.biology}</td>
                                <td>${data.exam.physics}</td>
                                <td>${data.exam.history}</td>
                                <td>${data.exam.geography}</td>
                                <td>${data.exam.cre}</td>
                                <td>${data.exam.agriculture}</td>
                                <td>${data.exam.business}</td>
                                <td>${data.exam.total}</td>
                            </tr>
                        </table>
                    </div>
                `;
                if (status === '200'){
                    document.getElementById('rank').innerHTML = rank;
                }
                else{
                    console.log(message);
                    raiseError(message);
                }
                });
                })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
}
