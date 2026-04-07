import axios from "axios";
import React, { use, useState } from "react";
import { API } from "./api";

const Log = ()=>{

    const [logData, setLogData] = useState({
        email: "",
        password: ""
    });
    const [msg, setMsg] = useState("")

    const handleData = (e)=>{
        setLogData({
            ...logData, 
            [e.target.name]:e.target.value
        });
    };

    const handleLoginApi = async (e)=>{
        e.preventDefault();

        try {
            const response = axios.post(`${API}/signinapp/login/`,logData);
            setMsg(response.data.msg);

        } catch (error) {
            setMsg(error.response?.data?.msg || "something wrong");
        }
    };


    return(
        <>

        <h1>Login form</h1>
        <form onSubmit={handleLoginApi}>

            <input
                type="email"
                name="email"
                placeholder="enter eamail"
                value={logData.email}
                onChange={handleData}
            />

            <input
                type="password"
                name="password"
                placeholder="enter password"
                value={logData.password}
                onChange={handleData}
            />
            <button>Hit Me Hard Yar</button>

        </form>
        </>
    )
};

export default Log;

