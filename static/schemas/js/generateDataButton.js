let generateButton = document.querySelector('#Generate-data')
generateButton.addEventListener('click', generateData)
let url = 'http://127.0.0.1:8000/'

let csrfToken
fetch(`${url}get_csrf_token/`)
  .then(response => response.json())
  .then(data => {
    csrfToken = data.csrf_token;
  });

function generateData(){
    const content = getData()

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
        body: JSON.stringify(content)
      };
    
    fetch(`${url}generate_data/`, options)
        .then(response => {
            if (!response.ok) {
            throw new Error('error');
            }
            return response.json();
        })
        .catch(error => {
            console.log(Error)
        });
}


function getData(){
    const content = new Object

    const url = window.location.href; // получаем текущий URL
    const urlObject = new URL(url); // создаем объект URL из строки
    const schemaID = urlObject.pathname.split('/')[2]

    const amountRows = document.querySelector('#count-rows .input-text').value
    
    content['schemaID'] = schemaID
    content['amountRows'] = amountRows

    return content
}


