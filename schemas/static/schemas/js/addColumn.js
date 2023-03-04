let buttonAddColumn = document.querySelector('#add-column')

buttonAddColumn.addEventListener('click', function(event){
    let oneColumn = document.querySelector('.new-schema-third-block .block-columns-select');
    let cloneColumn= oneColumn.cloneNode(true);

    let secondBlock = document.querySelector('.new-schema-second-block');
    secondBlock.append(cloneColumn);

    // order +1
    const orderValue = document.querySelector('.new-schema-third-block .block-del-order .input-text');
    orderValue.value = parseInt(orderValue.value) + 1;
});

