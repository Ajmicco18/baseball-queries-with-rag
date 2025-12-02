import { useState } from 'react'
import axios from "axios";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';

const BASE_URL = import.meta.env.VITE_API_URL

function App() {

  const [query, setQuery] = useState("")
  const [resp, setResp] = useState("")
  const [isResponse, setIsResponse] = useState(false)

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`${BASE_URL}/chat`, {
        query: query
      })
      console.log(response.data[0])
      setResp(response.data[0])
      setIsResponse(true)
    }
    catch (error) {
      console.error("Error: ", error)
    }

    setQuery("")
  }

  const handleReset = () => {
    setResp("")
    setIsResponse(false)
  }

  return (
    <>
      <h1 style={{ textAlign: "center", color: "#D50032" }}>Baseball Queries Website</h1>
      <Box display={"flex"} margin={"auto"} flexDirection={"column"} justifyContent={"center"} alignItems={"center"} width={"80%"}>
        {isResponse ? (
          <>
            <TextField
              disabled
              value={resp}
              sx={{ color: "black", backgroundColor: "white" }}
            />
            <Button onClick={handleReset} sx={{ mt: "5px", backgroundColor: "white", color: "#D50032", "&:hover": { backgroundColor: "#D50032", color: "white" } }}>Reset</Button>
          </>
        ) : (
          <>
            <TextField
              value={query}
              onChange={event => setQuery(event.target.value)}
              sx={{ color: "black", backgroundColor: "white" }} />
            <Button onClick={handleSubmit} sx={{ mt: "5px", backgroundColor: "white", color: "#D50032", "&:hover": { backgroundColor: "#D50032", color: "white" } }}>Query</Button>
          </>
        )}
      </Box >
    </>
  )
}

export default App
