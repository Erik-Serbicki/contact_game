import React from 'react';
import { Grid, Button, Typography } from "@mui/material";
import { useLoaderData } from 'react-router-dom';

export default function Lobby(){

    const data = useLoaderData();

    return(
        <Typography>Main Lobby: {data.code} </Typography>
    );
}