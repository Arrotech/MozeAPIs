document.getElementById('getSubjects').addEventListener('click', getSubjects);

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

    function getSubjects(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            fetch('http://localhost:5000/api/v1/portal/subjects' ,{
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
                data.subjects.forEach(subject => {
                    let status = data['status'];
                    let message = data['message'];
                    const { subject_id, admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business } = subject;
                        output += `
                            <div>
                                <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Registration No: ${subject.admission_no}</h4>
                                <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Exam ID: ${subject.subject_id}</h4>
                                <table>
                                    <tr>
                                        <th>Subjects</th>
                                        <th>Marks</th>
                                    </tr>
                                    <tr>
                                        
                                        <td>Mathematics</td>
                                        <td>${subject.maths}</td>
                                    </tr>
                                    <tr>
                                        <td>English</td>
                                        <td>${subject.english}</td>
                                    </tr>
                                    <tr>
                                        <td>Kiswahili</td>
                                        <td>${subject.kiswahili}</td>
                                    </tr>
                                    <tr>
                                        <td>Chemistry</td>
                                        <td>${subject.chemistry}</td>
                                    </tr>
                                    <tr>
                                        <td>Biology</td>
                                        <td>${subject.biology}</td>
                                    </tr>
                                    <tr>
                                        <td>Physics</td>
                                        <td>${subject.physics}</td>
                                    </tr>
                                    <tr>
                                        <td>History</td>
                                        <td>${subject.history}</td>
                                    </tr>
                                    <tr>
                                        <td>Geography</td>
                                        <td>${subject.geography}</td>
                                    </tr>
                                    <tr>
                                        <td>Cre</td>
                                        <td>${subject.cre}</td>
                                    </tr>
                                    <tr>
                                        <td>Agriculture</td>
                                        <td>${subject.agriculture}</td>
                                    </tr>
                                    <tr>
                                        <td>Business</td>
                                        <td>${subject.business}</td>
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