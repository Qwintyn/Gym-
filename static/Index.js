
    // Fetch data for dropdown 1
    fetch('http://127.0.0.1:5000/Users', {mode:"cors"})
      .then(response => response.json())
      .then(data => {
        const dropdown1 = document.getElementById('dropdown1');
        data.forEach(option => {
          const optionElement = document.createElement('option');
          optionElement.value = option.value;
          optionElement.textContent = option.label;
          dropdown1.appendChild(optionElement);
        });
      });

    // Fetch data for dropdown 2
