import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'

function Nav() {
    return (
        <>
            <Box
                width={"100%"}
                margin={"auto"}
                display={"flex"}
                flexDirection={"row"}
                justifyContent={"left"}
                alignItems={"center"}
                sx={{ background: 'linear-gradient(to right, white, #002D72)' }}>
                <img src='./baseball.png' style={{ padding: "10px" }} height={"75px"} width={"75px"}></img>
                <Typography variant='h4' component={"h4"} sx={{ color: "#D50032" }}>
                    RAG Baseball Queries
                </Typography>
            </Box>
        </>
    )
}

export default Nav
