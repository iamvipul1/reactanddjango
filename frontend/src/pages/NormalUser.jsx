import { useNavigate } from "react-router-dom";

function NormalUser() {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('ACCESS_TOKEN');
        localStorage.removeItem('REFRESH_TOKEN');
        navigate('/login');
    };

    return (
        <div>
            <h1>Welcome, Normal User!</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default NormalUser;
