document.addEventListener('DOMContentLoaded', function () {
    const classifyButton = document.getElementById('classify-button');
    const ticketText = document.getElementById('ticket-text');
    const resultDiv = document.getElementById('result');
    const predictionElement = document.getElementById('prediction');

    classifyButton.addEventListener('click', function () {
        const text = ticketText.value.trim();

        if (text !== '') {
            fetch('/classify', {
                method: 'POST',
                body: new URLSearchParams({ 'ticket_text': text }),
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
            })
                .then(response => response.json())
                .then(data => {
                    predictionElement.textContent = data.prediction;
                    resultDiv.classList.remove('hidden');
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    });
});
