// 0-promise.js
function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Here, you would typically make an API request
    // For simplicity, let's resolve the Promise immediately
    resolve('Response from API');
  });
}

export default getResponseFromAPI;
