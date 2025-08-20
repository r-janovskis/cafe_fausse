import axios from "axios";

const BASE_URL = "http://localhost:5000";
function getMenu() {
  const url = "/api/menu";
  //console.log(`Making request to: ${url}`);
  return axios.get(BASE_URL + url);
}

const apiServices = {
  getMenu,
};

export default apiServices;
