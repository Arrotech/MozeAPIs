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
                const { admission_no, term, form, type, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business } = exam;
                rank += `
                    <div>
                        <table>
                            <tr>
                                <th>Admission No.</th>
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
                            </tr>
                            <tr>
                                <td>${exam.admission_no}</td>
                                <td>${exam.term}</td>
                                <td>${exam.form}</td>
                                <td>${exam.type}</td>
                                <td>${exam.maths}</td>
                                <td>${exam.english}</td>
                                <td>${exam.kiswahili}</td>
                                <td>${exam.chemistry}</td>
                                <td>${exam.biology}</td>
                                <td>${exam.physics}</td>
                                <td>${exam.history}</td>
                                <td>${exam.geography}</td>
                                <td>${exam.cre}</td>
                                <td>${exam.agriculture}</td>
                                <td>${exam.business}</td>
                            </tr>
                        </table>
                    </div>
                `;
                if (status === '200'){
                    document.getElementById('rank').innerHTML = rank;
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
