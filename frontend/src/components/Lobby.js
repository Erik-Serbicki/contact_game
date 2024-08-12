import React, { useEffect } from 'react';
import { Grid, Button, Typography } from "@mui/material";
import { useLocation } from 'react-router-dom';

export default function Lobby(){

    const { data } = useLocation(); 
    console.log(data);

    return(
        <Grid container spacing={2} align="center">
            <Grid item xs={12}>
                <Typography>Main Lobby</Typography>
            </Grid>
        </Grid> 
    );
}