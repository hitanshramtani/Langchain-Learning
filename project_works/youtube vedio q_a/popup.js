document.addEventListener("DOMContentLoaded", () => {
    const askBtn = document.getElementById("askBtn");
    const answerBox = document.getElementById("answer");
  
    askBtn.addEventListener("click", async () => {
      const question = document.getElementById("question").value;
  
      // Get current YouTube tab's URL
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      const video_url = tab.url;
  
      try {
        const response = await fetch("http://localhost:8000/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ video_url, question })
        });
  
        const data = await response.json();
        answerBox.innerText = data.answer;
      } catch (error) {
        answerBox.innerText = "Something went wrong. Check your backend.";
        console.error("Error:", error);
      }
    });
  });
  