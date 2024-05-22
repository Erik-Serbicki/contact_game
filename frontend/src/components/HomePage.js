import React from "react";
import { createBrowserRouter, RouterProvider, Link, redirect} from "react-router-dom";
import { Button, Grid, Typography, ButtonGroup} from "@mui/material";

export default function HomePage(){

    const router = createBrowserRouter([
        {
            path: "/",
            element: renderHomeScreen(),
        },
    ]);

    function renderHomeScreen(){
        return (
            <Grid container spacing={3} align="center">
                <Grid item xs={12}>
                    <Typography variant="h2" component="h2">
                        Contact: The Game
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <Button color="primary" variant="outlined" >
                        Create a Room
                    </Button>
                    </Grid>
                <Grid item xs={12}>
                    <Button color="secondary" variant="outlined">
                        Join a Room
                    </Button>
                </Grid>
            </Grid>
        );
    }

    return(
        <RouterProvider router={router} />
    );
}