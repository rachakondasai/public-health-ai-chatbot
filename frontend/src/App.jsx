import React, { useState } from 'react';

export default function App() {
  const [msg, setMsg] = useState('');
  const [chat, setChat] = useState([]);

  async function send() {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    setChat([...chat, { q: msg, a: data.reply }]);
    setMsg('');
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>Public Health Chatbot</h2>
      <input value={msg} onChange={e => setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
      <div>
        {chat.map((c, i) => (
          <div key={i}>
            <p><b>You:</b> {c.q}</p>
            <p><b>Bot:</b> {c.a}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
