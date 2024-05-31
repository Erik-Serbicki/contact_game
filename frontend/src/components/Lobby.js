import React from 'react';
import { Grid, Button, Typography } from "@mui/material";
import { useLoaderData } from 'react-router-dom';

export default function Lobby(){

    const data = useLoaderData();
    console.log(data);

    return(
        <Grid container spacing={2} align="center">
            <Grid item xs={12}>
                <Typography>Main Lobby: {data.room.code} </Typography>
                <Typography>Nickname: {data.user.user_name} </Typography>
            </Grid>
        </Grid> 
    );
}