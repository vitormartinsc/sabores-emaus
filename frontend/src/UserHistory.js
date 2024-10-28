import React, { useEffect, useState } from 'react';

const UserHistory = ({ user }) => {
    const [orders, setOrders] = useState([]);
    console.log(user)
    useEffect(() => {
        console.log(user)
        const fetchOrders = async () => {
            const response = await fetch(`http://localhost:5000/orders?username=${user.username}`);
            const data = await response.json();
            setOrders(data);
        };

        fetchOrders();
    }, [user.username]);

    return (
        <div>
            <h1>Histórico de Pedidos de {user.name}</h1>
            <table>
                <thead>
                    <tr>
                        <th>Data</th>
                        <th>Pedido</th>
                        <th>Quantidade</th>
                    </tr>
                </thead>
                <tbody>
                    {orders.map((order, index) => (
                        <tr key={index}>
                            <td>{order.date}</td>
                            <td>{order.name_item}</td>
                            <td>{order.quantity}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default UserHistory;
