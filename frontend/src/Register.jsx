import React, {useState} from 'react';
import axios from 'axios';
import { API } from './api';

const Register = ()=>{

    
    const [formData, setFormData] = useState({
        username:"",
        email:"",
        password:""
    });
    
    const [msg, setMsg] = useState("");
    
    
    const hanldeData = (e)=>{
        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        });
    };
    
    
    const handleApi = async (e)=>{
        e.preventDefault();
    
        try {
            
            const data = await axios.post(`${API}`,formData);
            setMsg(data.data.msg);
    
        } catch (error) {
            setMsg(error?.response?.data?.msg || "something went wrong");
        }
    };
    
    return(
        <>
        <h1>Register..!</h1>
    
        <form onSubmit={handleApi}>
    
            <input className='in'
                type='text' 
                name='username' 
                placeholder='username' 
                value={formData.username} 
                onChange={hanldeData}
            />
    
            <input className='in'
                type='email'
                name='email'
                placeholder='email'
                value={formData.email}
                onChange={hanldeData}
            />
    
            <input className='in'
                type='password'
                name='password'
                placeholder='password'
                value={formData.password}
                onChange={hanldeData}
            />
    
        </form>
    
        </>
    );
};



export default Register;


