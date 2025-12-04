import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import GitHubIcon from '@mui/icons-material/GitHub';
import IconButton from '@mui/material/IconButton';

function Footer() {
    const year = new Date().getFullYear()

    return (
        <>
            <Box width={"100%"} margin={"auto"} textAlign={"center"} sx={{ position: "fixed", bottom: 0, left: 0 }}>
                <Stack direction={"row"} display={"flex"} alignItems={"center"} justifyContent={"center"}>
                    <Typography variant='h6' component={'h6'} color="#D50032">
                        &copy; {year} Anthony Micco
                    </Typography>
                    <IconButton size='large' href="https://github.com/Ajmicco18/baseball-queries-with-rag" >
                        <GitHubIcon sx={{ color: "#D50032", "&:hover": { color: "white" } }} />
                    </IconButton>
                </Stack>
            </Box>
        </>
    )
}

export default Footer
