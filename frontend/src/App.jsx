import React, { useState } from "react";
import "./styles.css";
import developerImg from "./assets/image.png";

export default function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  async function sendMessage() {
    if (!message.trim()) return;

    const userMsg = message.trim();
    setChat((prev) => [...prev, { role: "user", text: userMsg }]);
    setMessage("");

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMsg }),
      });

      const data = await res.json();
      setChat((prev) => [...prev, { role: "bot", text: data.reply }]);
    } catch (err) {
      setChat((prev) => [
        ...prev,
        {
          role: "bot",
          text: "⚠️ Backend not reachable. Please run FastAPI on http://localhost:8000",
        },
      ]);
    }
  }

  return (
    <div className="app-container">
      {/* Header */}
      <header className="topbar">
        <div className="topbar-inner">
          <div>
            <h1>Public Health Awareness Chatbot</h1>
            <span>AI-Driven Disease Awareness System</span>
          </div>
          <div className="badge">Academic Project • v1.0</div>
        </div>
      </header>

      {/* Main Content */}
      <div className="main-layout">
        {/* Chat Section */}
        <section className="chat-section">
          <div className="chat-header">Chat Assistant</div>

          <div className="chat-window">
            {chat.length === 0 && (
              <div className="chat-placeholder">
                👋 Welcome! <br />
                Type a disease name like <b>Dengue</b>, <b>Malaria</b>, or ask about{" "}
                <b>Symptoms & Prevention</b>.
              </div>
            )}

            {chat.map((c, i) => (
              <div key={i} className={`chat-bubble ${c.role}`}>
                {c.text}
              </div>
            ))}
          </div>

          <div className="chat-input">
            <input
              placeholder="Type your question here..."
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </section>

        {/* Info Panel */}
        <aside className="info-panel">
          <h3>Supported Topics</h3>
          <ul>
            <li>Dengue</li>
            <li>Malaria</li>
            <li>COVID-19</li>
            <li>Flu</li>
            <li>Symptoms & Prevention</li>
          </ul>

          <h3>System Purpose</h3>
          <p>
            This system provides public health awareness, prevention guidance, and
            emergency indicators. It does not replace medical consultation.
          </p>

          <div className="alert-box">
            ⚠️ Educational Use Only <br />
            Not a medical diagnosis system
          </div>
        </aside>
      </div>

      {/* Footer */}
      <footer className="footer">
        <div className="developer-card">
          <img src={developerImg} alt="Developer G Nikhil Raju" />
          <div className="dev-text">
            <strong>Developed by G Nikhil Raju</strong>
            <span>B.Tech CSE – Final Year</span>
            <span>REVA University</span>
            <span className="dev-mini">Public Health AI Chatbot • 2025</span>
          </div>
        </div>
      </footer>
    </div>
  );
}