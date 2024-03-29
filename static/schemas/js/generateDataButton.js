let generateButton = document.querySelector('#Generate-data')
generateButton.addEventListener('click', generateNewDataSet)
// let url = 'http://dsmyronchuk.pythonanywhere.com/'
let url = 'http://127.0.0.1:8000/'

function generateNewDataSet(){
    const [processingBlock, downloadBlock] = addRowToPage()
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
        .then(data=>{
          updateStatusROw(processingBlock, downloadBlock, data.schema_name, data.data_set_pk)
        })
        .catch(error => {
            console.log(Error)
        });
}


function getData(){
    const content = new Object

    const url = window.location.href;
    const urlObject = new URL(url);
    const schemaID = urlObject.pathname.split('/')[2]

    const amountRows = document.querySelector('#count-rows .input-text').value
    
    content['schemaID'] = schemaID
    content['amountRows'] = amountRows

    return content
}


function addRowToPage(){
  const table = document.querySelector('#data-sets');
  const allNumber = table.querySelectorAll('.table-numeric');
  let number = 1
 
  if (allNumber.length != 0){
    number = parseInt(allNumber[allNumber.length - 1].textContent) +1
  }
 
  const date = new Date().toISOString().slice(0, 10);

  table.insertAdjacentHTML(
    'beforeend',
    `
    <tbody>
    <tr>
        <td class="col-1 table-numeric">${number}</td>
        <td class="col-2">${date}</td>
        <td class="col-2">
            <div id="processing-${number}" class="dataset-processing">Processing</div>
        </td>
        <td class="col-2 download-csv" id="download-${number}"></td>
    </tr>
</tbody>	
    `
  )

  const processingBlock = table.querySelector(`#processing-${number}`);
  const downloadBlock = table.querySelector(`#download-${number}`);
  return [processingBlock, downloadBlock];
}

function updateStatusROw(processingBlock, downloadBlock, schema_name, data_set_pk){
  processingBlock.outerHTML = '<div class="dataset-ready">Ready</div>';
  downloadBlock.innerHTML = `<a href="/download_csv/${schema_name}/${data_set_pk}/">Download</a>`
}