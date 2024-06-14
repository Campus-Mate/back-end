import React, { useState } from 'react';
import axios from 'axios';

const SendID = () => {
  const [id, setId] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [title, setTitle] = useState('');
  const [responseData, setResponseData] = useState(null);
  const [checkId, setCheckId] = useState('');
  const [checkTitle, setCheckTitle] = useState('');
  const [checkResponse, setCheckResponse] = useState([]);
  const [checkIdOnly, setCheckIdOnly] = useState('');
  const [checkIdOnlyResponse, setCheckIdOnlyResponse] = useState([]);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://3.37.222.122:8001/api/receive_id/', { id_value: id, title, content, category }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      setResponseData(response.data);
      console.log(response.data);
    } catch (error) {
      console.error('There was an error sending the ID!', error);
    }
  };

  const handleCheckIdAndTitle = async () => {
    try {
      const response = await axios.post('http://3.37.222.122:8001/api/show_id/', { id_value: checkId, title: checkTitle }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      setCheckResponse(response.data);
      setError(null);
    } catch (error) {
      setError('Record not found');
      setCheckResponse([]);
    }
  };

  const handleCheckIdOnly = async () => {
    try {
      const response = await axios.post('http://3.37.222.122:8001/api/show_id_by_id/', { id_value: checkIdOnly }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      setCheckIdOnlyResponse(response.data);
      setError(null);
    } catch (error) {
      setError('Record not found');
      setCheckIdOnlyResponse([]);
    }
  };

  const handleDelete = async (idValue) => {
    try {
      await axios.delete('http://3.37.222.122:8001/api/delete_id/', {
        headers: {
          'Content-Type': 'application/json',
        },
        data: { id_value: idValue }
      });
      setCheckResponse(checkResponse.filter(record => record.id_value !== idValue));
      setError(null);
    } catch (error) {
      setError('Failed to delete record');
      console.error('There was an error deleting the ID!', error);
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
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter title. no limit"
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
        <button type="submit">Send Data</button>
      </form>
      
      {responseData && (
        <div>
          <h3>Response Data:</h3>
          <p>ID: {responseData.id_value}</p>
          <p>Title: {responseData.title}</p>
          <p>Content: {responseData.content}</p>
          <p>Category: {responseData.category}</p>
          <p>Created At: {responseData.created_at}</p>
        </div>
      )}
      
      <div>
        <input
          type="text"
          value={checkId}
          onChange={(e) => setCheckId(e.target.value)}
          placeholder="Enter ID to check"
        />
        <input
          type="text"
          value={checkTitle}
          onChange={(e) => setCheckTitle(e.target.value)}
          placeholder="Enter title to check"
        />
        <button onClick={handleCheckIdAndTitle}>Check ID and Title</button>
      </div>
      
      {checkResponse.length > 0 && (
        <div>
          <h3>Record Details</h3>
          {checkResponse.map(record => (
            <div key={record.id}>
              <p>ID: {record.id_value}</p>
              <p>Title: {record.title}</p>
              <p>Content: {record.content}</p>
              <p>Category: {record.category}</p>
              <p>Created At: {record.created_at}</p>
              <button onClick={() => handleDelete(record.id_value)}>Delete</button>
            </div>
          ))}
        </div>
      )}

      <div>
        <input
          type="text"
          value={checkIdOnly}
          onChange={(e) => setCheckIdOnly(e.target.value)}
          placeholder="Enter ID to check only by ID"
        />
        <button onClick={handleCheckIdOnly}>Check ID Only</button>
      </div>
      
      {checkIdOnlyResponse.length > 0 && (
        <div>
          <h3>Record Details by ID</h3>
          {checkIdOnlyResponse.map(record => (
            <div key={record.id}>
              <p>ID: {record.id_value}</p>
              <p>Title: {record.title}</p>
              <p>Content: {record.content}</p>
              <p>Category: {record.category}</p>
              <p>Created At: {record.created_at}</p>
            </div>
          ))}
        </div>
      )}
      
      {error && <p>{error}</p>}
    </div>
  );
};

export default SendID;
