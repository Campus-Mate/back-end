// frontend/src/components/SendID.js
import React, { useState } from 'react';
import axios from 'axios';

const SendID = () => {
  const [id, setId] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');
  

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/receive_id/', { id,content,category,date }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      console.log(response.data);
    } catch (error) {
      console.error('There was an error sending the ID!', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={id}
          onChange={(e) => setId(e.target.value)}
          placeholder="Enter ID. max length 255"
        />
        <input
          type="text"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          placeholder="Enter content. no limit"
        />
        <input
          type="text"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          placeholder="Enter category. max length 255"
        />
        <input
          type="text"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          placeholder="Enter date. YYYY-MM-DD"
        />
        <button type="submit">Send Data</button>
      </form>
    </div>
  );
};

export default SendID;
