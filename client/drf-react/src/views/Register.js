import { useState } from 'react';
import axiosInstance from '../axios';
import { useNavigate, NavLink } from 'react-router-dom';

export default function Register() {
	const navigate = useNavigate();
	
    const initialFormData = Object.freeze({
		email: '',
		username: '',
		password: '',
        password2: '',
	});

	const [formData, setFormData] = useState(initialFormData);

	const handleChange = (e) => {
		setFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const onSubmitForm = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance.post(`accounts/register`, {
				email: formData.email,
				username: formData.username,
				password: formData.password,
                password2: formData.password2,
			})
			.then((res) => {
				navigate.push('/login');
				console.log(res);
				console.log(res.data);
			});
	};

	return (
			<div className='container'>
				
				<h3>Register</h3>

				<form onSubmit={onSubmitForm} noValidate>
                    <div className="mb-3">
                        <label htmlFor="email">Email</label>
                        <input type="email" id='email' name='email' onChange={handleChange} className="form-control" />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="username">Username</label>
                        <input type="text" id='username' name='username' onChange={handleChange} className="form-control" />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="first_name">First Name</label>
                        <input type="text" id='first_name' name='first_name' onChange={handleChange} className="form-control" />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="last_name">Last Name</label>
                        <input type="text" id='last_name' name='last_name' onChange={handleChange} className="form-control" />
                    </div>
                    
                    <div className="mb-3">
                        <label htmlFor="password">Password</label>
                        <input type="password" id='password' name='password' onChange={handleChange} className="form-control" />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="password2">Password Confirm</label>
                        <input type="password" id='password2' name='password2' onChange={handleChange} className="form-control" />
                    </div>
					<button type="submit">Register</button>
					
                    <NavLink to="/login">
                        Already have an account? Sign in
                    </NavLink>
				</form>
			</div>
	);
}