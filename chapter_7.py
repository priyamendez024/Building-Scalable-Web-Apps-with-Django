
# Chapter 7: Frontend Integration & Modern JavaScript

# Example React Component to fetch products from Django API
import React, { useState, useEffect } from 'react';

function ProductList() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('/api/products/')
            .then(response => response.json())
            .then(data => setProducts(data));
    }, []);

    return (
        <ul>
            {products.map(product => (
                <li key={product.id}>{product.name}</li>
            ))}
        </ul>
    );
}

export default ProductList;
    