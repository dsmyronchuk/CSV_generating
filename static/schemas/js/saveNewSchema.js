let btnSubmit = document.querySelector('#NewSchema-submit')
btnSubmit.addEventListener('click', saveNewSchema)
// let url = 'http://dsmyronchuk.pythonanywhere.com/'
let url = 'http://127.0.0.1:8000/'


function saveNewSchema(){
    const content = getData()

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
        body: JSON.stringify(content)
      };

    let errorSpace = document.querySelector('#error-space'); // Get the error space element
    
    // check min/max value in Integer columns 
    for (let column in content.allColumns) {
        if (content.allColumns[column][0] === 'Integer') {
            let min = parseInt(content.allColumns[column][2]);
            let max = parseInt(content.allColumns[column][3]);

            if (min > max) {
                errorSpace.innerHTML = 'The minimum value should be less than the maximum value';
                return; // Stop the function execution
            }
        }
    }
    
    fetch(`${url}save_schema/`, options)
        .then(response => {
            if (!response.ok) {
            throw new Error('Check the completed data. All fields must be filled. Schema Name field and Column name must be unique');
            }
            return response.json();
        })
        .then(data => {
            window.location.replace(`${url}/`)
        })
        .catch(error => {
            if (errorSpace.innerHTML == ''){
                errorSpace.innerHTML = error;
            }
        });

}   


function getData(){
    let content = new Object

    const userIdInput = document.querySelector('script[data-user-id]');
    const userId = userIdInput.getAttribute('data-user-id');

    let schemaName = document.querySelector('.new-schema-top .input-text').value 
    let columnSeparator = document.querySelector('#column-separator').textContent;
    let stringCharacter = document.querySelector('#string-character').textContent;
    content['userId'] = userId
    content['nameSchema'] = schemaName
    content['columnSeparator'] = columnSeparator
    content['stringCharacter'] = stringCharacter

    let secondBlock = document.querySelector('.new-schema-second-block')
    let allRows = secondBlock.querySelectorAll('.block-columns-select')

    let allColumns = new Object
    for (let i=0; i < allRows.length; i++){
        const columnName = allRows[i].querySelector('.left-block .input-text').value;
        const columnType = allRows[i].querySelector('.center-block .selected-value').textContent;
        const orderColumn = allRows[i].querySelector('.block-del-order .input-text').value;
        if (columnType !== 'Integer'){
          allColumns[columnName] = [columnType, orderColumn];
        }
        else{
          const min = allRows[i].querySelector('.functional-left .input-text').value;
          const max = allRows[i].querySelector('.functional-right .input-text').value;
          allColumns[columnName] = [columnType, orderColumn, min, max];
        }
    }
    content['allColumns'] = allColumns
    return content
  }

