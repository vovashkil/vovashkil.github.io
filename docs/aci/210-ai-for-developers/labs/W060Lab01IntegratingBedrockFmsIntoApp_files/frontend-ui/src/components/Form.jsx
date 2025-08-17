import React, { useState } from 'react';
import './Form.css';
import axios from 'axios';
import ErrorMessage from './ErrorMessage';

function extractJsonArray(responseText) {
  // Use a regular expression to find the JSON array in the string
  const jsonArrayMatch = responseText.match(/\[\s*\{.*\}\s*\]/s);

  if (jsonArrayMatch) {
    try {
      // Parse the matched JSON array string
      const jsonArray = JSON.parse(jsonArrayMatch[0]);
      return jsonArray;
    } catch (e) {
      console.error("Failed to parse JSON array:", e);
      return null;
    }
  } else {
    console.error("No JSON array found in the response.");
    return null;
  }
}

function convertToJson(inputString) {
  try {
    // Step 1: Parse the initial JSON string to a JavaScript object
    const parsedObject = JSON.parse(inputString);
    console.log("Parsed JSON object:", parsedObject);

    // Step 2: Handle API Gateway response format with statusCode, headers, body
    let dataObject = parsedObject;
    if (parsedObject.statusCode && parsedObject.body) {
      // Parse the body string to get the actual data
      dataObject = JSON.parse(parsedObject.body);
      console.log("Parsed body object:", dataObject);
    }

    // Step 3: Check if the dataObject has the expected structure
    if (Array.isArray(dataObject) && dataObject.length > 0) {
      // The dataObject is an array, so we can directly return it
      return dataObject;
    } else if (dataObject.results && dataObject.results.length > 0) {
      // Step 4: Extract the message property
      const messageString = dataObject.results[0].outputText;
      console.log("Message string:", messageString);

      // Extract the JSON array from the message string
      const jsonString = extractJsonArray(messageString);
      return jsonString || [];
    } else {
      console.error("Unexpected response format:", dataObject);
      return [];
    }
  } catch (error) {
    console.error("Error parsing JSON:", error);
    return [];
  }
}

const Form = ({ setFlashcards }) => {
  const [notes, setNotes] = useState('');
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null); // Reset the error state
    setIsLoading(true); // Set the loading state to true

    // Check if the API Gateway endpoint is set
    if (!process.env.REACT_APP_API_GATEWAY_ENDPOINT_URL) {
      setError('API Gateway endpoint not found. Please set the REACT_APP_API_GATEWAY_ENDPOINT_URL environment variable.');
      setIsLoading(false); // Set the loading state to false
      return;
    }

    try {
      const response = await axios.post(process.env.REACT_APP_API_GATEWAY_ENDPOINT_URL, {
        notes: notes
      });

      console.log('Response:', response.data);
      console.log('response.data is this', JSON.stringify(response.data));

      const flashcardsArray = convertToJson(JSON.stringify(response.data));
      setFlashcards(flashcardsArray);
      setIsLoading(false); // Set the loading state to false
    } catch (error) {
      console.error('Error:', error);
      setIsLoading(false); // Set the loading state to false

      // Check if the error is related to Bedrock rate limits
      if (error.response && error.response.data && error.response.data.error) {
        setError(`Bedrock error: ${error.response.data.error}`);
      } else {
        setError('An unexpected error occurred.');
      }
    }
  };

  return (
    <div className='form-container'>
      {error && <ErrorMessage message={error} />}
      <form className='form' onSubmit={handleSubmit}>
        <div>
          <label htmlFor="notes">Drop your study notes here</label>
          <textarea
            name="notes"
            id="notes"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
          />
        </div>
        <button style={{ cursor: "pointer" }} type="submit" disabled={isLoading}>
          {isLoading ? 'Generating flashcards...' : 'Generate flashcards'}
        </button>
      </form>
    </div>
  );
};

export default Form;