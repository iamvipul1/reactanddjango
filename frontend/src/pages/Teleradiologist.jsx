import { useNavigate } from "react-router-dom";

function Teleradiologist() {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem('ACCESS_TOKEN');
        localStorage.removeItem('REFRESH_TOKEN');

        navigate('/login');
    };

    return (
        <div>
            <h1>Welcome, Teleradiologist!</h1>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Teleradiologist;