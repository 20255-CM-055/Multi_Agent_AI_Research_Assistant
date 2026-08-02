import axios from "axios";

// const API = "http://localhost:8000";
const API = "http://localhost:8000/api/v1";

export async function sendMessage(researchId, message) {
    const response = await axios.post(
        `${API}/chat/${researchId}`,
        {
            message,
        }
    );

    return response.data;
}