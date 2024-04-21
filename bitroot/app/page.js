"use client"
import { useState } from "react"
export default function Home() {
  const [inputText, setInputText] = useState('');
  const [responseText, setResponseText] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleSendClick = async () => {
    try {
        const response = await fetch('https://bitroot-pkrfjsbe6q-el.a.run.app/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: inputText }),  
        });
        const data = await response.json();
        console.log(data)
        setResponseText(data.response);
    } catch (error) {
        console.error('Error:', error);
        setResponseText('Error fetching data');
    }
  };

  return (
    <div>
      <input type="text" value={inputText} onChange={handleInputChange} style={{ color: 'black' }} />
      <button onClick={handleSendClick}>Send</button>
      <div>{responseText}</div>
    </div>
  );
}
