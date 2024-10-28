import React, { useState } from 'react';
import Login from './Login';
import Welcome from './Welcome';

const App = () => {
    const [user, setUser] = useState(null); // Estado para armazenar as informações do usuário

    const handleLogin = (userData) => {
        setUser(userData); // Atualiza o estado com os dados do usuário
    };

    return (
        <div>
            {user ? (
                <Welcome user={user} /> // Passa as informações do usuário para o componente Welcome
            ) : (
                <Login onLogin={handleLogin} /> // Passa a função de login para o componente Login
            )}
        </div>
    );
};

export default App;
