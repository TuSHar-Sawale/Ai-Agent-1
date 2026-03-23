async function runAgent(task) {
    const filePath = document.getElementById("fileSelect").value;

    const res = await fetch("/run-agent", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            file_path: filePath,
            task: task
        })
    });

    if (!res.ok) {
        const text = await res.text();
        document.getElementById("output").textContent = "Error:\n" + text;
        return;
    }

    const data = await res.json();

    let output = "";
    data.forEach(step => {
        output += `\n=== ${step.step} ===\n${step.output}\n`;
    });

    document.getElementById("output").textContent = output;
}async function loadFiles() {
    const res = await fetch("/files");
    const files = await res.json();

    const select = document.getElementById("fileSelect");

    files.forEach(file => {
        const option = document.createElement("option");
        option.value = "test_project/" + file;
        option.textContent = file;
        select.appendChild(option);
    });
}

window.onload = loadFiles;