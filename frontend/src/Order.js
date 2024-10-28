import React, { useState } from 'react';

const Order = () => {
    const [name, setName] = useState('');
    const [cakeType, setCakeType] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('http://localhost:5000/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, cakeType }),
        });
        const data = await response.json();
        setMessage(data.message);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Nome" value={name} onChange={(e) => setName(e.target.value)} required />
            <select value={cakeType} onChange={(e) => setCakeType(e.target.value)} required>
                <option value="">Escolha um tipo</option>
                <option value="chocolate">Chocolate</option>
                <option value="baunilha">Baunilha</option>
                <option value="morango">Morango</option>
            </select>
            <button type="submit">Fazer Pedido</button>
            {message && <p>{message}</p>}
        </form>
    );
};

export default Order;
