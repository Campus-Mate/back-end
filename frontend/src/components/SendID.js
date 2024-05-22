// frontend/src/components/SendID.js
import React, { useState } from 'react';
import axios from 'axios';

const SendID = () => {
  const [id, setId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/receive_id/', { id }, {
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
          placeholder="Enter ID"
        />
        <button type="submit">Send ID</button>
      </form>
    </div>
  );
};

export default SendID;
