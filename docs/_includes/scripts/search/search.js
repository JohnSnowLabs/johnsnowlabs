/*!
  * Search
  * Licensed under the MIT License.
  */


'use strict'

function fetchAndPopulate() {
  // Fetch JSON data
  fetch('search.json')
      .then(response => response.json())
      .then(data => {
          // Process the JSON data
          populateHTML(data);
          // Now that data is loaded, add input event listener for searching
          document.getElementById('search-input').addEventListener('input', search);
      })
      .catch(error => console.error('Error fetching JSON:', error));
}



function populateHTML(data) {
  // Iterate through the data and create HTML elements
  const container = document.getElementById('results-container');
  container.innerHTML = ''; // Clear previous content

  data.forEach(item => {
      const element = document.createElement('li');
      element.innerHTML = `${item.demopage}<a href="${item.url}">${item.title}</a><div class="sr_seotitle">${item.seotitle}</div><em>${item.content}</em>`;
      container.appendChild(element);
  });
}



function search() {
  const searchTerm = document.getElementById('search-input').value.toLowerCase(),
        resultsContainer = document.getElementById('results-container'),
        itemsTitle = document.querySelectorAll('#results-container a'), 
        itemsContent = document.querySelectorAll('#results-container em'), 
        items = document.querySelectorAll('#results-container li'); 

        if(searchTerm.length > 3) {
          itemsTitle.forEach(item => {
            wrapWordInSpan(item, searchTerm);
          });
  
          itemsContent.forEach(item => {
            wrapWordInSpan(item, searchTerm);
          });
        }

      items.forEach(item => {
      
      const text = item.innerText.toLowerCase();
      
      if (text.includes(searchTerm) && searchTerm.length > 3) {        
          resultsContainer.style.display = 'block';
          item.style.display = 'block';
      } else {
          item.style.display = 'none';
      }
      if (searchTerm == "" || searchTerm == null) {
        resultsContainer.style.display = 'none';
    }
  });
  

}

function wrapWordInSpan(data, wordToWrap) {

  var dataText = data.textContent;

  var regex = new RegExp('(' + wordToWrap.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');


  var newText = dataText.replace(regex, '<span class="hightitle">$1</span>');

  // Замена содержимого элемента с новым текстом
  return data.innerHTML = newText;
}



