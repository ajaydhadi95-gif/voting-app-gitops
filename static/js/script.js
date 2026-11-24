
const message = document.getElementById("message");

async function loadResults() {
    try {
        const response = await fetch("/api/results");

        if (!response.ok) {
            throw new Error("Unable to load results");
        }

        const data = await response.json();

        document.getElementById("python-count").textContent =
            data.Python + " votes";

        document.getElementById("java-count").textContent =
            data.Java + " votes";

        document.getElementById("total-count").textContent =
            data.total;

        document.getElementById("python-bar").style.width =
            data.Python_percent + "%";

        document.getElementById("java-bar").style.width =
            data.Java_percent + "%";

    } catch (error) {
        message.textContent = "Could not load voting results.";
    }
}

async function castVote(choice) {
    const buttons = document.querySelectorAll(".vote-card button");

    buttons.forEach(button => button.disabled = true);

    try {
        const response = await fetch("/api/vote", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ choice: choice })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Vote failed");
        }

        message.textContent = "Successfully voted for " + choice + "!";

        await loadResults();

    } catch (error) {
        message.textContent = error.message;

    } finally {
        buttons.forEach(button => button.disabled = false);
    }
}

loadResults();

setInterval(loadResults, 5000);
