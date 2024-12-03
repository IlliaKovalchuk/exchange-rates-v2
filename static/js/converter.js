const form = document.getElementById('convertForm');
const resultDiv = document.getElementById('conversionResult');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const amount = document.getElementById('amount').value;
    const fromCurrency = document.getElementById('from_currency').value;
    const toCurrency = document.getElementById('to_currency').value;

    try {
        const response = await fetch(`/convert?amount=${amount}&from_currency=${fromCurrency}&to_currency=${toCurrency}`);
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<p style="color: red;">Помилка: ${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `<p>${amount} ${fromCurrency} = ${data.converted.toFixed(2)} ${toCurrency}</p>`;
        }
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">Помилка під час конвертації: ${error.message}</p>`;
    }
});
swapButton.addEventListener('click', () => {
    const fromCurrency = document.getElementById('from_currency');
    const toCurrency = document.getElementById('to_currency');
    [fromCurrency.value, toCurrency.value] = [toCurrency.value, fromCurrency.value];
});
