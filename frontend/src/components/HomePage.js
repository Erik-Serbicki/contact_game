import React from "react";
import { createBrowserRouter, RouterProvider, Link, redirect} from "react-router-dom";
import { Button, Grid, Typography, TextField, ThemeProvider, CssBaseline, createTheme, IconButton, Card, CardContent, Box, useMediaQuery, FormControl} from "@mui/material";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";
import Lobby from "./Lobby";

export default function HomePage(){
    const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

    const [state, setState] = React.useState({
        mode: prefersDarkMode ? 'dark':'light',
        userName: '', 
    });

    const getDesignTokens = (mode) => ({
        palette: {
            mode,
            ...(mode === 'light' ? {
                primary: {
                    main: "#470024",
                },
                secondary: {
                    main: "#846C5B",
                }, 
                background: {
                    default: "#E3D7FF",
                    paper: "#846C5B",
                },
            } : {
                primary: {
                    main: "#470024",
                }, 
                secondary: {
                    main: "#846C5B",
                }, 
                background: {
                    default: "#071E22",
                    paper: "#846C5B",
                },
                text: {
                    primary: "#E3D7FF"
                },
            }),
        }
    });

    const theme = React.useMemo(() => createTheme(getDesignTokens(state.mode)), [state.mode]);

    function changeMode(){
        setState(prevState => ({
            ...prevState, mode: state.mode === 'light' ? 'dark' : 'light',
        }));
    }

    function handleUserNameChange(e){
        setState(prevState => ({
            ...prevState, userName: e.target.value,
        }));
    }

    const router = createBrowserRouter([
        {
            path: "/",
            element: renderHomeScreen(),
        },
        {
            path: '/lobby',
            element: <Lobby />,
            loader: async () => {
                const [room, user] = await Promise.all([
                    fetch('/api/create-room', {method:"post", headers:{'Content-Type':'application/json'}}).then(res => res.json()),
                    fetch('/api/create-user', {
                        method:'post',
                        headers: {'Content-Type':'application/json'},
                        body: JSON.stringify({
                            user_name: state.userName,
                        }),
                    }).then(res => res.json())
                ]);

                return {user, room};  //ADD ERROR RESPONSE
            }
        },
    ]);

    function renderHomeScreen(){

        // const themeButtonBox = (
        //     <Box sx={{
        //         display:'flex', 
        //         alignItems:'center', 
        //         justifyContent: 'center', 
        //         bgcolor: 'background.paper', 
        //         maxWidth: 120,
        //         minHeight: 50,
        //         borderRadius: '8px',
        //         }}>
        //         <Typography variant="body2">{theme.palette.mode.toUpperCase()} MODE</Typography>
        //         <IconButton sx={{ ml: 1}} onClick={changeMode} color="inherit">
        //             {theme.palette.mode === 'dark' ? <Brightness7Icon/>:<Brightness4Icon/>}
        //         </IconButton>
        //     </Box>
        // );

        return (
            <Grid container align="center" spacing={3}>
                <Grid item xs={12}>
                    <Typography component={'h1'} variant="h1">
                        Contact: The Word Game
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <FormControl>
                        <Typography variant="h4" component="h4">Choose a cool nickname</Typography>
                        <TextField label="Name" variant="outlined" onChange={handleUserNameChange}/>
                    </FormControl>
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" color="primary" to='/lobby' component={Link}>
                        Play
                    </Button>
                </Grid>
                {/* <Grid item xs={12}>
                    {themeButtonBox}
                </Grid> */}
            </Grid> 
        );
    }

    const themeButtonBox = (
        <Box sx={{
            display:'flex', 
            alignItems:'center', 
            justifyContent: 'center', 
            bgcolor: 'background.paper', 
            maxWidth: 120,
            minHeight: 50,
            borderRadius: '8px',
            }}>
            <Typography variant="body2">{theme.palette.mode.toUpperCase()} MODE</Typography>
            <IconButton sx={{ ml: 1}} onClick={changeMode} color="inherit">
                {theme.palette.mode === 'dark' ? <Brightness7Icon/>:<Brightness4Icon/>}
            </IconButton>
        </Box>
    );

    return(
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <RouterProvider router={router} />  
            {themeButtonBox}
        </ThemeProvider>
    );
}