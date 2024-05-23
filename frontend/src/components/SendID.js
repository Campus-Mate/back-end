import React, { useState } from 'react';
import axios from 'axios';

const SendID = () => {
  const [id, setId] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [responseData, setResponseData] = useState(null); // 서버에서 받은 데이터를 저장할 상태
  const [checkId, setCheckId] = useState(''); // 확인할 ID를 저장할 상태
  const [checkResponse, setCheckResponse] = useState(null); // ID 확인 결과를 저장할 상태
  const [error, setError] = useState(null);

  // 데이터 전송 함수
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/receive_id/', { id_value: id, content, category }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      setResponseData(response.data);  // 서버에서 받은 데이터를 상태에 저장
      console.log(response.data);
    } catch (error) {
      console.error('There was an error sending the ID!', error);
    }
  };

  // ID 확인 함수
  const handleCheckId = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/check_id/', { id_value: checkId }, {
        headers: {
          'Content-Type': 'application/json',
        }
      });
      setCheckResponse(response.data);
      setError(null);
    } catch (error) {
      setError('Record not found');
      setCheckResponse(null);
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
        
        <button type="submit">Send Data</button>
      </form>
      
      {responseData && (
        <div>
          <h3>Response Data:</h3>
          <p>ID: {responseData.id_value}</p>
          <p>Content: {responseData.content}</p>
          <p>Category: {responseData.category}</p>
          <p>Created At: {responseData.created_at}</p> {/* created_at 필드 표시 */}
        </div>
      )}
      
      <div>
        <input
          type="text"
          value={checkId}
          onChange={(e) => setCheckId(e.target.value)}
          placeholder="Enter ID to check"
        />
        <button onClick={handleCheckId}>Check ID</button>
      </div>
      
      {checkResponse && (
        <div>
          <h3>Record Details</h3>
          <p>ID: {checkResponse.id_value}</p>
          <p>Content: {checkResponse.content}</p>
          <p>Category: {checkResponse.category}</p>
          <p>Created At: {checkResponse.created_at}</p>
        </div>
      )}
      
      {error && <p>{error}</p>}
    </div>
  );
};

export default SendID;
