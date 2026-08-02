import api from "../api/axios";

export async function generateResearch(query) {
  const response = await api.post("/research", {
    query,
  });

  return response.data;
}

export async function getHistory() {
  const response = await api.get("/history");

  return response.data;
}

export async function getResearchById(id) {
  const response = await api.get(`/history/${id}`);

  return response.data;
}

// export function streamResearch(query, onMessage, onError) {
//   // const eventSource = new EventSource(
//   //   `http://127.0.0.1:8000/research/stream?query=${encodeURIComponent(query)}`
//   // );
//   const eventSource = new EventSource(
//   `http://127.0.0.1:8000/api/v1/research/stream?query=${encodeURIComponent(query)}`
// );

//   // eventSource.onmessage = (event) => {
//   //   const data = JSON.parse(event.data);
//   //   onMessage(data);
//   // };

  

//   eventSource.onerror = (error) => {
//     eventSource.close();

//     if (onError) {
//       onError(error);
//     }
//   };

//   return eventSource;
// }


export function streamResearch(query, onMessage, onError) {
  const eventSource = new EventSource(
    `http://127.0.0.1:8000/api/v1/research/stream?query=${encodeURIComponent(query)}`
  );

  eventSource.onmessage = (event) => {
    console.log("========== SSE ==========");
    console.log(event.data);

    const data = JSON.parse(event.data);

    console.log("PARSED:", data);

    onMessage(data);
  };

  eventSource.onerror = (error) => {
    console.error("SSE ERROR:", error);

    eventSource.close();

    if (onError) {
      onError(error);
    }
  };

  return eventSource;
}


export async function deleteResearch(id) {
  await api.delete(`/history/${id}`);
}