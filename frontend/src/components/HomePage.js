import React from "react";
import { createBrowserRouter, RouterProvider, Link, redirect} from "react-router-dom";
import { Button, Grid, Typography, Card, TextField, ThemeProvider, CssBaseline, createTheme, useTheme, IconButton} from "@mui/material";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";

export default function HomePage(){
    const [state, setState] = React.useState({
        mode: 'light',
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

    const router = createBrowserRouter([
        {
            path: "/",
            element: renderHomeScreen(),
        },
    ]);

    function renderHomeScreen(){
        return (
            <Grid container align="center" spacing={3}>
                <Grid item xs={12}>
                    <Typography component={'h1'} variant="h1">
                        Contact: The Word Game
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <Typography variant="h4" component="h4">Choose a cool nickname</Typography>
                    <TextField label="Name" variant="outlined"/>
                </Grid>
                <Grid item xs={12}>
                    <Button variant="contained" color="primary">
                        Play
                    </Button>
                </Grid>
                <Grid item xs={12}>
                    <p>{theme.palette.mode} mode</p>
                    <IconButton sx={{ ml: 1 }} onClick={changeMode} color="inherit">
                        {theme.palette.mode === 'dark' ? <Brightness7Icon/>:<Brightness4Icon/>}
                    </IconButton>
                </Grid>
            </Grid> 
        );
    }

    return(
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <RouterProvider router={router} />  
        </ThemeProvider>
    );
}