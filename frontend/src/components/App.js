import React from "react";

export default function App()
{
    return (<h1>Hello There!</h1>);
}

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(< App tab="home"/>);