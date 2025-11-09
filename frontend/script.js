// ...existing code...
import 'bootstrap/dist/css/bootstrap.min.css';
// ...existing code...
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('bmi-form');
  const resultDiv = document.getElementById('result');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);

    if (!weight || !height) {
      resultDiv.textContent = 'Please enter valid weight and height.';
      return;
    }

    try {
      const res = await fetch(`/calculate?w=${encodeURIComponent(weight)}&h=${encodeURIComponent(height)}`);
      if (!res.ok) {
        resultDiv.textContent = `Server error: ${res.status}`;
        return;
      }
      const data = await res.json();
      resultDiv.innerHTML = `<p>Your BMI: <strong>${data.bmi}</strong></p><p>Category: <strong>${data.category}</strong></p>`;
    } catch (err) {
      console.error(err);
      resultDiv.textContent = 'Error calculating BMI';
    }
  });
});