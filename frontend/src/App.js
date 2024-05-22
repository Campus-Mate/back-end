// frontend/src/App.js
import React from 'react';
import SendID from './components/SendID';

const App = () => {
    return (
        <div>
            <h1>Send ID to Django</h1>
            <SendID />
        </div>
    );
};

export default App;
