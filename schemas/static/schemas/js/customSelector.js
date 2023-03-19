let firstBlock = document.querySelector('.wrap');
firstBlock.addEventListener('click', cusSelector);

function cusSelector(event) {
  let target = event.target;

  if (!target.closest('.custom-select')) return;  // return if click not on arrow

  let customSelect = target.closest('.custom-select');
  let select = customSelect.querySelector('select');
  let selected = customSelect.querySelector('.selected-value');
  let options = select.querySelectorAll('option');

  let currentIndex = customSelect.dataset.currentIndex || 0;
  
  if (target.classList.contains('btn-up')) {
    if (currentIndex < options.length - 1) {
      currentIndex++;
      selected.innerHTML = options[currentIndex].innerHTML;
      select.value = options[currentIndex].value;
      customSelect.dataset.currentIndex = currentIndex;
    }
  }
  if (target.classList.contains('btn-down')) {

    if (currentIndex > 0) {
        currentIndex--;
      selected.innerHTML = options[currentIndex].innerHTML;
      select.value = options[currentIndex].value;
      customSelect.dataset.currentIndex = currentIndex;
    }
  }

  checkOrder(selected);

}


function checkOrder (selected){
  const functionalBlock = document.querySelector('.new-schema-third-block .functional-block')
  const functionalLeft = document.querySelector('.new-schema-third-block .functional-left')
  const functionalRight = document.querySelector('.new-schema-third-block .functional-right')

  if (selected.innerHTML == 'Integer' && !functionalBlock.contains(functionalLeft)){
    functionalBlock.insertAdjacentHTML(
      'afterbegin',
      `
      <div class="functional-left">
          <div class="column-name">From</div>
          <input class="input-text" type="text" name="{{schema}}">
      </div>
      <div class="functional-right">
          <div class="column-name">To</div>
          <input class="input-text" type="text" name="{{schema}}">
      </div>
      `
    )
  }
  else if(selected.innerHTML != 'Integer' && functionalBlock.contains(functionalLeft)){
    functionalLeft.remove();
    functionalRight.remove();
  }
}