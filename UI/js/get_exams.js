document.getElementById('getExams').addEventListener('click', getExams);

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

    function getExams(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');
            admission_no = window.localStorage.getItem('admission_no');
            exam_id = window.localStorage.getItem('exam_id');

            fetch('http://localhost:5000/api/v1/exams' ,{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let output = `<h3 style="margin-left: 10px;"> Exams grouped by Subjects.</h3>`;
                data.exams.forEach(exam => {
                    let status = data['status'];
                    let message = data['message'];
                    const { exam_id, admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business } = exam;
                    if (message === 'successfully retrieved'){
                        output += `
                            <div>
                                <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Registration No: ${exam.admission_no}</h4>
                                <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Exam ID: ${exam.exam_id}</h4>
                                <table>
                                    <tr>
                                        <th>Subjects</th>
                                        <th>Marks</th>
                                    </tr>
                                    <tr>
                                        <td>Mathematics</td>
                                        <td>${exam.maths}</td>
                                    </tr>
                                    <tr>
                                        <td>English</td>
                                        <td>${exam.english}</td>
                                    </tr>
                                    <tr>
                                        <td>Kiswahili</td>
                                        <td>${exam.kiswahili}</td>
                                    </tr>
                                    <tr>
                                        <td>Chemistry</td>
                                        <td>${exam.chemistry}</td>
                                    </tr>
                                    <tr>
                                        <td>Biology</td>
                                        <td>${exam.biology}</td>
                                    </tr>
                                    <tr>
                                        <td>Physics</td>
                                        <td>${exam.physics}</td>
                                    </tr>
                                    <tr>
                                        <td>History</td>
                                        <td>${exam.history}</td>
                                    </tr>
                                    <tr>
                                        <td>Geography</td>
                                        <td>${exam.geography}</td>
                                    </tr>
                                    <tr>
                                        <td>Cre</td>
                                        <td>${exam.cre}</td>
                                    </tr>
                                    <tr>
                                        <td>Agriculture</td>
                                        <td>${exam.agriculture}</td>
                                    </tr>
                                    <tr>
                                        <td>Business</td>
                                        <td>${exam.business}</td>
                                    </tr>
                                </table>
                            </div>
                        `;

                        document.getElementById('output').innerHTML = output;
                    }else{
                        raiseError(message)
                    }
                    });
                    })
            .catch((err)=>{
                raiseError("Please check your internet connection and try again!");
                console.log(err);
            })
    }
