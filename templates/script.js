async function sendQuestion(questionText = null) {
    const input = document.getElementById("question-input");
    const chatList = document.getElementById("chat-list");

    const question = questionText || input.value.trim();
    if (!question) return;

    // User message
    const userDiv = document.createElement("div");
    userDiv.className = "chat-box";
    userDiv.innerHTML = `<div class="user-message">${question}</div>`;
    chatList.appendChild(userDiv);
    input.value = "";

    // Bot loading
    const botDiv = document.createElement("div");
    botDiv.className = "chat-box";
    const botMsg = document.createElement("div");
    botMsg.className = "bot-message";
    botMsg.textContent = "Typing...";
    botDiv.appendChild(botMsg);
    chatList.appendChild(botDiv);

    chatList.scrollTop = chatList.scrollHeight;

    try {
        const res = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await res.json();

        if (!data.answer || data.answer.trim() === "") {
            botMsg.textContent = "⚠️ Error: No answer received. ";

            const retryBtn = document.createElement("button");
            retryBtn.textContent = "Retry";
            retryBtn.style.marginLeft = "10px";
            retryBtn.style.padding = "5px 10px";
            retryBtn.style.border = "none";
            retryBtn.style.borderRadius = "6px";
            retryBtn.style.background = "#007bff";
            retryBtn.style.color = "white";
            retryBtn.style.cursor = "pointer";

            retryBtn.onclick = () => {
                input.value = question;
                input.focus();
                sendQuestion(question);
            };

            botMsg.appendChild(retryBtn);
        } else {
            botMsg.textContent = data.answer;
        }

    } catch (err) {
        botMsg.textContent = "❌ Failed to get a response from the server.";
    }

    chatList.scrollTop = chatList.scrollHeight;
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("question-input").addEventListener("keypress", function (e) {
        if (e.key === "Enter") sendQuestion();
    });
});
