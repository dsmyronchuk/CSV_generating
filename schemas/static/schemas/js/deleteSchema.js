let deleteButtons = document.querySelectorAll('.actions-block .delete');
let url = 'http://dsmyronchuk.pythonanywhere.com/'

for (let i = 0; i < deleteButtons.length; i++ ){
    deleteButtons[i].addEventListener('click', deleteShema);
}



function deleteShema(event){
    let obj = event.currentTarget.getAttribute("row");

    const options = {
        method: 'Delete',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
      };

    fetch(`${url}delete_schema/${obj}/`, options)
    .then(response => {
        if (!response.ok) {
        throw new Error('Schema does not exists');
        }
        return response.json();
    })
    .then(data => {
        updatePageAfterDelete(event);
    })
}

function updatePageAfterDelete(event){
    row = event.target.closest('tr');
    row.remove();
}