
const form = document.getElementById("chatForm");
const input = document.getElementById("msg");
const sendBtn = document.getElementById("sendBtn");
const messages = document.getElementById("messages");
const welcome = document.getElementById("welcome");

form.addEventListener("submit", function (event) {
    event.preventDefault();
    send();
});

function askQuestion(question) {
    input.value = question;
    send();
}

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = "message " +
        (sender === "user" ? "user-message" : "bot-message");

    const avatar = document.createElement("div");
    avatar.className = "avatar " +
        (sender === "user" ? "user-avatar" : "bot-avatar");
    avatar.textContent = sender === "user" ? "Y" : "E";

    const body = document.createElement("div");
    body.className = "message-body";

    const name = document.createElement("div");
    name.className = "message-name";
    name.textContent = sender === "user" ? "You" : "EduMate";

    const content = document.createElement("div");
    content.className = "message-text";
    content.textContent = text;

    body.appendChild(name);
    body.appendChild(content);

    message.appendChild(avatar);
    message.appendChild(body);

    messages.appendChild(message);
    message.scrollIntoView({
        behavior: "smooth",
        block: "nearest"
    });

    return message;
}

function showTyping() {
    const message = document.createElement("div");
    message.className = "message";
    message.id = "typingIndicator";

    message.innerHTML = `
        <div class="avatar bot-avatar">E</div>
        <div class="message-body">
            <div class="message-name">EduMate</div>
            <div class="typing">
                <span></span><span></span><span></span>
            </div>
        </div>
    `;

    messages.appendChild(message);
    message.scrollIntoView({
        behavior: "smooth",
        block: "nearest"
    });
}

async function send() {
    const question = input.value.trim();

    if (!question || sendBtn.disabled) {
        return;
    }

    welcome.style.display = "none";
    messages.classList.add("visible");

    addMessage(question, "user");
    input.value = "";
    sendBtn.disabled = true;
    input.disabled = true;

    showTyping();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: question
            })
        });

        const data = await response.json();

        document.getElementById("typingIndicator")?.remove();

        if (!response.ok) {
            throw new Error(data.response || "Request failed");
        }

        addMessage(
            data.response || "No response was returned.",
            "bot"
        );

    } catch (error) {
        document.getElementById("typingIndicator")?.remove();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

        console.error("Chat error:", error);

    } finally {
        sendBtn.disabled = false;
        input.disabled = false;
        input.focus();
    }
}

function newChat() {
    messages.replaceChildren();
    messages.classList.remove("visible");
    welcome.style.display = "";
    input.value = "";
    input.focus();
}

