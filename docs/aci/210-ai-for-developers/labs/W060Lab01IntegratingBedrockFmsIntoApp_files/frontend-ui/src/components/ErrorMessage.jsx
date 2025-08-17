// src/components/ErrorMessage.jsx
import React from 'react';

const ErrorMessage = ({ message }) => {
  return (
    <div style={{ color: 'red', marginBottom: '10px' }}>
      <strong>Error:</strong> {message}
    </div>
  );
};

export default ErrorMessage;