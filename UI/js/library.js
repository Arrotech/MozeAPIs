document.getElementById('getBooks').addEventListener('click', getBooks);

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

    function getBooks(event){
            event.preventDefault();

            token = window.localStorage.getItem('token');

            fetch('http://localhost:5000/api/v1/books' ,{
                method: 'GET',
                headers : {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token,
                },
            })
            .then((res) => res.json())
            .then((data) => {
                let output = `<h3 style="margin-left: 10px;"> Books grouped by Admission Number.</h3>`;
                data.books.forEach(book => {
                    let status = data['status'];
                    let message = data['message'];
                    const { book_id, admission_no, author, title, subject } = book;
                    output += `
                        <div>
                            <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Registration No: ${book.admission_no}</h4>
                            <h4 style="margin-left: 10px; text-decoration:none; color: #d65050;">Exam ID: ${book.book_id}</h4>
                            <table>
                                <tr>
                                    <th>Author</th>
                                    <th>Title</th>
                                    <th>Subject</th>
                                </tr>
                                <tr>
                                    <td>${book.author}</td>
                                    <td>${book.title}</td>
                                    <td>${book.subject}</td>
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
