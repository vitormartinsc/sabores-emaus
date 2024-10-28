import React, { useState } from 'react';
import UserHistory from './UserHistory';

const Welcome = ({ user }) => {
    const [showHistory, setShowHistory] = useState(false);

    const handleViewHistory = () => {
        setShowHistory(true); // Mostra o componente UserHistory
    };

    return (
        <div>
            <h1>Bem-vindo, {user.name}!</h1>
            <p>O que você gostaria de fazer?</p>
            <button onClick={() => alert('Fazer pedido')}>Fazer pedido</button>
            <button onClick={handleViewHistory}>Ver pedidos anteriores</button>

            {showHistory && <UserHistory userId={user.id} />} 
        </div>
    );
};

export default Welcome;


