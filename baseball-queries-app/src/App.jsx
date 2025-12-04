import { useState } from 'react'
import axios from "axios";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import Footer from './components/footer';
import Nav from './components/Nav';

const BASE_URL = import.meta.env.VITE_API_URL

function App() {

  const [query, setQuery] = useState("")
  const [resp, setResp] = useState("")
  const [isResponse, setIsResponse] = useState(false)
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async () => {
    setIsLoading(true)
    try {
      const response = await axios.post(`${BASE_URL}/chat`, {
        query: query
      })
      console.log(response.data.Response)
      setResp(response.data.Response)
      setIsResponse(true)
      setIsLoading(false)
      setQuery("")
    }
    catch (error) {
      console.error("Error: ", error)
      setIsLoading(false)
    }
  }

  const handleReset = () => {
    setResp("")
    setIsResponse(false)
  }

  return (
    <>
      <Nav />
      <Container sx={{ width: "100%", mt: "50px" }}>
        <Box display={"flex"} margin={"auto"} flexDirection={"column"} justifyContent={"center"} alignItems={"center"} width={"80%"}>
          {isResponse ? (
            <>
              <Box width={"100%"} padding={"15px"} margin={"auto"} textAlign={"center"} sx={{ backgroundColor: "white", borderRadius: "5px" }}>
                <Typography variant='p' component={"p"} fontSize={"16px"} fontWeight={"bold"} color='black'>
                  {resp}
                </Typography>
              </Box>
              <Button onClick={handleReset} sx={{ mt: "10px", width: "25%", backgroundColor: "white", color: "#D50032", "&:hover": { backgroundColor: "#D50032", color: "white" } }}>Reset</Button>
            </>
          ) : (
            <>
              <TextField
                value={query}
                onChange={event => setQuery(event.target.value)}
                fullWidth
                placeholder='Enter a baseball related question!'
                sx={{ color: "black", backgroundColor: "white", borderRadius: "5px" }} />
              {isLoading ? (
                <Stack sx={{ mt: "10px" }} direction={"row"} display={"flex"} flexDirection={"row"} alignItems={"center"} justifyContent={"center"}>
                  <img src='./Spinner.svg' height={"80px"} width={"80px"}></img>
                  <Typography variant='p' component={"p"} fontSize={"25px"}>Thinking...</Typography>
                </Stack>
              )
                :
                (<Button onClick={handleSubmit} sx={{ mt: "10px", width: "25%", backgroundColor: "white", color: "#D50032", "&:hover": { backgroundColor: "#D50032", color: "white" } }}>Query</Button>)
              }
            </>
          )}
        </Box >
      </Container>
      <Footer />
    </>
  )
}

export default App
