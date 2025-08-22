import axios from "axios";

const BASE_URL = "http://localhost:5000";
function getMenu() {
  const endpoint = "/api/menu";
  //console.log(`Making request to: ${url}`);
  return axios.get(BASE_URL + endpoint);
}

function subscribeToNewsletter(email) {
  const endpoint = "/api/newsletter";

  return axios.post(BASE_URL + endpoint, { email });
}

const apiServices = {
  getMenu,
  subscribeToNewsletter,
};

export default apiServices;
