import { useState } from 'react';
import axiosInstance from '../axios';
import { useNavigate, NavLink } from 'react-router-dom';

export default function Register() {
	const navigate = useNavigate();
	
    const initialFormData = Object.freeze({
		email: '',
		password: '',
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

		axiosInstance.post(`accounts/token`, {
				email: formData.email,
				password: formData.password,
			})
			.then((res) => {
                localStorage.setItem('access_token', res.data.access);
				localStorage.setItem('refresh_token', res.data.refresh);
				axiosInstance.defaults.headers['Authorization'] = 'Bearer ' + localStorage.getItem('access_token');
				navigate.push('/');
				console.log(res);
			});
	};

	return (
			<div className='container'>
				
				<h3>Login</h3>

				<form onSubmit={onSubmitForm} noValidate>
                    <div className="mb-3">
                        <label htmlFor="email">Email</label>
                        <input type="email" id='email' name='email' onChange={handleChange} className="form-control" />
                    </div>

                    <div className="mb-3">
                        <label htmlFor="password">Password</label>
                        <input type="password" id='password' name='password' onChange={handleChange} className="form-control" />
                    </div>

					<button type="submit">Login</button>
					
                    <NavLink to="/register">
                        No account? Register
                    </NavLink>
				</form>
			</div>
	);
}