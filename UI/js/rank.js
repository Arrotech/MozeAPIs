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
        exam_id = window.localStorage.getItem('exam_id');

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
                let status = data['status'];
                let message = data['message'];
                rank = `
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
                                <td>${data.Exam.admission_no}</td>
                                <td>${data.Exam.term}</td>
                                <td>${data.Exam.form}</td>
                                <td>${data.Exam.type}</td>
                                <td>${data.Exam.maths}</td>
                                <td>${data.Exam.english}</td>
                                <td>${data.Exam.kiswahili}</td>
                                <td>${data.Exam.chemistry}</td>
                                <td>${data.Exam.biology}</td>
                                <td>${data.Exam.physics}</td>
                                <td>${data.Exam.history}</td>
                                <td>${data.Exam.geography}</td>
                                <td>${data.Exam.cre}</td>
                                <td>${data.Exam.agriculture}</td>
                                <td>${data.Exam.business}</td>
                            </tr>
                        </table>
                    </div>
                `;
                if (status === '200'){
                    document.getElementById('rank').innerHTML = rank;
                }else{
                    raiseError(message);
                }
                })
        .catch((err)=>{
            raiseError("Please check your internet connection and try again!");
            console.log(err);
        })
}
