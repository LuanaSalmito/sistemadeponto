// Exemplo de componente ou função de Logout
import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext'; // Importa useAuth
import { Nav } from 'react-bootstrap';
function Logout() {
    const navigate = useNavigate();
    const { setIsLoggedIn } = useAuth(); // Usa setIsLoggedIn
    const MAIN_URL = process.env.REACT_APP_MAIN;
    const handleLogout = () => {
        setIsLoggedIn(false); // Atualiza o estado de autenticação
        navigate(MAIN_URL + 'login');
    };

    return (
        <Nav.Link as="button" className="text-dark" onClick={handleLogout}>
            Sair
        </Nav.Link>
    );
}

export default Logout;
