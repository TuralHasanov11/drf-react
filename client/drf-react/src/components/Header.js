import {NavLink, useNavigate} from 'react-router-dom'
import axiosInstance from '../axios';

function Header(){

    const navigate = useNavigate();

    const logout = ()=>{
        const response = axiosInstance.post('account/logout/blacklist', {
			refresh_token: localStorage.getItem('refresh_token'),
		});
		localStorage.removeItem('access_token');
		localStorage.removeItem('refresh_token');
		axiosInstance.defaults.headers['Authorization'] = null;
		navigate.push('/login');
    }

    return <header>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
            <NavLink className={`navbar-brand`} to={'/'}>Home</NavLink>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                {/* <li className="nav-item">
                    <NavLink className={`nav-link ${({isActive}) => (isActive ? "active" : '')}}`} to={'/'}>All Meetups</NavLink>
                </li> */}
                <li className="nav-item">
                    <button className="nav-link btn btn-danger" onClick={logout}>Logout</button>
                </li>
            </ul>
            </div>
        </div>
        </nav>
    </header>
}

export default Header