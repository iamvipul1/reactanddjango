import { useNavigate } from "react-router-dom";

function Surgeon() {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('ACCESS_TOKEN');
        localStorage.removeItem('REFRESH_TOKEN');

        navigate('/login');
    };

    return (
        <div>
            <h1>Welcome, Surgeon!</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Surgeon;